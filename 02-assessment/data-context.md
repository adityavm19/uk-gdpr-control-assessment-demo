**Portfolio Case Study — All organisations, people, systems, evidence, findings and management responses in this repository are fictional or synthetic. This repository demonstrates GRC / IT audit methodology and does not represent a real client audit, certification audit, legal opinion or regulatory assurance engagement.**

# Processing & Data Context

The assessment uses six selected processing activities to anchor Article 32 testing in the nature, scope, context and purpose of processing rather than treating security measures as abstract controls. The highest-risk data sets are customer identity, account/transaction data, authentication records, fraud case information and identity-document evidence.

## Canonical systems most relevant to personal-data security
- `MT-APP-001` Microsoft Entra ID — identity control plane.
- `MT-APP-011` Meridian Core Banking Platform — customer account/transaction records.
- `MT-APP-012` Meridian Digital Banking — customer channel.
- `MT-APP-018` Meridian Customer CRM — customer/contact/case data.
- `MT-APP-019` ServiceNow Privacy Case Management — rights and privacy-incident workflow.
- `MT-APP-005` Microsoft Sentinel — security monitoring.
- `MT-APP-015` Azure Backup / Recovery Services — recovery capability.

## ROPA boundary
`ropa-extract.csv` is deliberately a **sample ROPA extract**, not a full legal Article 30 inventory. It contains the security/accountability fields needed for this portfolio workstream and does not represent a legal sufficiency opinion.
