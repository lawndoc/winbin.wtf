---
title: calc.exe
description: A basic calculator application with a GUI.
file-size:
    min: 27KB
    max: 27KB
signature: None
spawned-by:
    - explorer.exe
spawns:
    - none
lol-bin: No
references:
    - name: none
      link: https://example.com/link
acknowledgements:
    - name: C.J. May
      handle: lawndoc
---

## Description

{{ page.description }}

## Properties

**File Size**: {{ page.file-size.min }} - {{ page.file-size.max }}

**Digital Signature**: {{ page.signature }}

**Spawned by**:
{%- for parent in page.spawned-by -%}
- {{ parent }}
{%- endfor -%}

**Spawns**:
{%- for child in page.spawns -%}
- {{ child }}
{%- endfor -%}

**LoL Bin**: {{ page.lol-bin }}

## References

{%- for ref in page.references -%}
- [{{ ref.name }}]({{ ref.link }})
{%- endfor -%}

## Acknowledgements
{%- for person in page.acknowledgements -%}
- {{ person.name }} (@{{person.handle}})
{%- endfor -%}