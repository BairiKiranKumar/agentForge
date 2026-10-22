---
id: webgl-3d-scenes-three
type: motion
title: WebGL and 3D scenes with Three.js
summary: Render a lightweight 3D object or shader background in a canvas, driven by scroll or pointer, when depth is the actual message.
tags: [webgl, three, 3d, shader, canvas]
industries: [product, gaming, automotive, architecture]
scope: universal
sources:
  - url: https://threejs.org/manual/
    retrieved: 2026-10-22
    method: fetched-html
    note: only the header and navigation of the manual page came back; the minimal-scene page returned 404, so the code API below is not verified against fetched docs
  - url: https://motionsites.ai/
    retrieved: 2026-10-22
    method: fetched-html
    note: marketing page lists 3D and scroll-driven 3D template categories; labels only, no implementation detail
verified_on: 2026-10-22
verification: Three.js manual body was not retrieved, so the snippet is from general knowledge and marked [Unverified]; no rendering performed
status: current
constraints: Requires WebGL support; asset weight and GPU load; Three.js is MIT licensed [Unverified here]
license_notes: Original minimal snippet; no copied scenes or models
dependencies: three (version not verified; check npm for the current release)
performance: GPU and main-thread both matter; cap devicePixelRatio, limit draw calls, compress textures and models, pause when off-screen
accessibility: Provide text equivalent and static poster; no essential info only in 3D; reduced-motion users get a still or slow rotation off; avoid flashing
fallback: Static image or short video poster; detect WebGL failure and show the poster
when_to_use: Products or spaces where rotation, depth or lighting is the point of the page
when_not_to_use: Decorative backgrounds with no meaning, low-power or older devices, content sites where load time and battery matter, anything where a photo suffices
---

## What it is
A WebGL renderer, scene, camera and loop that draws into a canvas.

## Why it works
When the audience needs to judge form, 3D communicates faster than photos. It is expensive, so earn it.

## How to apply
Assumes a current `three` release; [Unverified] API names below.

```js
import * as THREE from "three";
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, innerWidth / innerHeight, 0.1, 100);
camera.position.z = 4;
renderer.setAnimationLoop(() => renderer.render(scene, camera));
```

## Performance guidance
No Three.js performance page was fetched, so the budget is [Inference]: cap pixel ratio, compress assets, one scene per page, pause off-screen. Canvas size must be reserved to prevent CLS. Lazy-initialise after first paint so LCP is not the canvas (web.dev LCP: late large elements reset it). Per-frame JS and event handlers compete with INP-measured interactions (web.dev INP).

## Accessibility
Static alternative and caption. Honour prefers-reduced-motion by not auto-rotating. SC 2.2.2: auto-playing motion longer than five seconds needs a pause control.

## Risks and limits
Battery drain, thermal throttling, driver variance, WebGL context loss.

## Related
scroll-synced-canvas-frame-sequence, pinned-scroll-storytelling, parallax-scroll-layers
