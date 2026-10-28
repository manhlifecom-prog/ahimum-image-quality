#!/usr/bin/env python3
"""Validate review evidence, not image quality. Never sends or changes assets."""
import argparse
import hashlib
import json
from pathlib import Path

WEIGHTS = [15, 10, 20, 10, 10, 10, 10, 5, 5, 5]
GATES = ('anatomy', 'identity', 'product', 'material', 'physics', 'text_logo',
         'obvious_ai', 'background_realism', 'prop_context', 'commercial_suitability', 'photographic_realism')


def validate(data, base):
    errors = []
    def issue(label, message):
        errors.append(f'{label}: {message}')
    def check_file(record, label):
        if not isinstance(record, dict):
            issue(label, 'file record required'); return
        name, expected = record.get('path'), record.get('sha256')
        if not name or not expected:
            issue(label, 'path and SHA256 required'); return
        path = Path(name)
        if not path.is_absolute():
            path = base / path
        if not path.is_file():
            issue(label, f'missing file {path}'); return
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            issue(label, 'SHA256 mismatch; review does not describe this file')
    images = data.get('images', [])
    expected_count = data.get('expectedImageCount')
    if not isinstance(expected_count, int) or expected_count <= 0:
        issue('set', 'expectedImageCount must be positive integer')
    elif len(images) != expected_count:
        issue('set', f'actual records {len(images)} != expected {expected_count}')
    if not images:
        issue('set', 'no images')
    for key in ('modelId', 'strictLookId', 'scope', 'story', 'setReview'):
        if not data.get(key):
            issue('set', f'missing {key}')
    sr = data.get('setReview', {})
    for key in ('identity', 'product', 'material', 'lighting', 'camera', 'story_variety'):
        x = sr.get(key, {}) if isinstance(sr, dict) else {}
        if x.get('status') != 'pass' or not x.get('evidence'):
            issue('set', f'{key} needs actual set-review evidence and pass')
    ids = set()
    for index, img in enumerate(images, 1):
        label = img.get('assetId') or f'image-{index}'
        if label in ids:
            issue(label, 'duplicate assetId')
        ids.add(label)
        check_file(img, label)
        for key in ('version', 'reviewer', 'reviewedAt', 'method', 'sourceSuitabilityEvidence'):
            if not img.get(key):
                issue(label, f'missing {key}')
        if img.get('strictLookId') != data.get('strictLookId'):
            issue(label, 'strictLook differs from set lock')
        for role in ('person_product', 'fabric', 'background'):
            sources = img.get('sources', {}).get(role, [])
            if not sources:
                issue(label, f'missing {role} source evidence')
            for ref in sources:
                check_file(ref, f'{label}/{role}')
                if role == 'background' and not ref.get('origin'):
                    issue(label, 'background origin/provenance required')
        if data.get('requiresRealBackground', True) and img.get('backgroundMethod') not in ('real-photo-kept', 'real-photo-composite'):
            issue(label, 'real photographic background required; generated reference is insufficient')
        scores = img.get('scores')
        valid_scores = isinstance(scores, list) and len(scores) == 10
        if valid_scores:
            valid_scores = all(isinstance(v, (int, float)) and not isinstance(v, bool) and 0 <= v <= w for v, w in zip(scores, WEIGHTS))
        if not valid_scores:
            issue(label, 'ten numeric scores within rubric weights required')
        else:
            total = sum(scores)
            if total <= 85:
                issue(label, f'{total}/100 is not strictly >85')
            if img.get('total') != total:
                issue(label, 'total does not equal ten components')
        gates = img.get('gates', {})
        for gate in GATES:
            rec = gates.get(gate, {})
            if rec.get('status') != 'pass' or not rec.get('evidence'):
                issue(label, f'{gate} failed/unresolved or missing visual evidence')
        for key in ('hardRejects', 'unresolved'):
            if key not in img or not isinstance(img[key], list) or img[key]:
                issue(label, f'{key} must be explicitly empty after actual review')
        inspected = set(img.get('inspected', []))
        if not {'5-second', '50-percent', 'native-detail-100-200'} <= inspected:
            issue(label, 'whole image and native detail inspection not recorded')
        if img.get('status') != 'self-qc-pass':
            issue(label, 'not self-qc-pass')
        if img.get('humanApproved'):
            a = img.get('humanApproval', {})
            if a.get('sha256') != img.get('sha256') or not all(a.get(k) for k in ('reviewer', 'at', 'scope', 'evidence')):
                issue(label, 'human approval requires reviewer/time/scope/evidence and exact file hash')
    return errors


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('manifest', type=Path)
    args = ap.parse_args()
    try:
        data = json.loads(args.manifest.read_text())
        errors = validate(data, args.manifest.resolve().parent)
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        print(json.dumps({'recordsConsistent': False, 'error': str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps({'recordsConsistent': not errors, 'images': len(data.get('images', [])),
                      'errors': errors, 'limitation': 'Evidence-record validation only; no image inspection or human approval is performed.'}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
