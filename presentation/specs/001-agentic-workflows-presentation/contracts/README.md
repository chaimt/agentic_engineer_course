# Content Contracts: Agentic Workflows Presentation

**Feature**: 001-agentic-workflows-presentation  
**Date**: 2026-04-16

## Overview

This directory defines the interface contracts for presentation content. These schemas specify the format for section specifications, slide metadata, code examples, and presenter materials.

## Contract Files

1. **section-spec.schema.yaml** - Format for content specifications in `specs/sections/*.spec.md`
2. **slide-frontmatter.schema.yaml** - Slidev slide frontmatter structure
3. **code-example.contract.md** - Code example embedding and display format
4. **presenter-api.contract.md** - Presenter notes, demo scripts, and rehearsal materials

## Purpose

These contracts ensure:
- **Consistency**: All content follows the same structure
- **Validation**: Automated checks can verify compliance
- **Documentation**: Content authors understand required fields
- **Generation**: Build scripts can reliably transform specs → Slidev markdown

## Usage

Content authors write section specifications matching `section-spec.schema.yaml`. The build process validates against schemas, then generates Slidev markdown with frontmatter matching `slide-frontmatter.schema.yaml`.

See `quickstart.md` for practical workflow guidance.
