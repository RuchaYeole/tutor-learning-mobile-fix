# Tutor Learning Mobile Fix

A Tutor plugin for improving mobile and tablet responsiveness
of the Open edX Learning Micro-Frontend (MFE).

## Overview

This plugin injects custom CSS into the Learning MFE during
the Docker image build process.

It aims to improve the learning experience on smaller screens
by addressing layout overflow, sidebar positioning, and
course content alignment.

## Features

- Responsive layout for mobile devices.
- Improved course sidebar positioning.
- Vertical stacking of course content on mobile screens.
- Responsive images, videos, and embedded content.
- Additional tablet layout adjustments.

## Compatibility

- Tutor: 19.0.x
- Tutor MFE: 19.0.x
- Open edX: Sumac release environment

## Installation

Install the plugin in the Tutor Python environment:

```bash
pip install -e .
