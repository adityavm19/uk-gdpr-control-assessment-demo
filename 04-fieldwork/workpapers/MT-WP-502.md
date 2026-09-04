**Portfolio Case Study — All organisations, people, systems, evidence, findings and management responses in this repository are fictional or synthetic. This repository demonstrates GRC / IT audit methodology and does not represent a real client audit, certification audit, legal opinion or regulatory assurance engagement.**

# Privileged authentication Workpaper

**Workpaper ID:** MT-WP-502  
**Test ID:** MT-TST-502  
**Control / process:** GDPR-CTL-002  
**Evidence:** MT-EV-503;MT-EV-504

## Objective
Privileged access to systems processing personal information uses strong authentication and controlled exceptions commensurate with risk.

## Population and sampling
Population: 42 privileged identities in Entra/PAM scope. Sample: 42 of 42. Rationale: Full population because privileged identities are small, high impact and system-export testing was feasible.

## Procedure
Reviewed design documentation and source evidence; reconciled the stated population; tested selected attributes; investigated deviations; distinguished design from operating effectiveness.

## Evidence sufficiency
Evidence was considered relevant, timely for the assessment period and corroborated beyond inquiry. Where system-generated evidence was unavailable or incomplete, that limitation is reflected in the conclusion.

## Result
Partial - legacy access path bypassed MFA for 3 privileged identities.

## Conclusion
Design: Partially Effective. Operating effectiveness: Partially Effective. Exception MT-EXC-501 supports GDPR-FND-001.
