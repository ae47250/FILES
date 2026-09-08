# PathFinder program cards - final adjudication audit

Generated 2026-08-19T22:41:15Z. 116 reviewed, import-ready program cards covering the 116 remaining Purdue West Lafayette programs.

## Result

- **Packaging validation: PASS** against `importValidatedProgramCards` - 0 blockers.
- Cards: **116** (103 COMPLETE source records, 13 PARTIAL).
- Concept assignments: **527** in the reviewed baseline; **525** preserved unchanged, **81** added, **1** removed, **1** re-roled - **83** total deviations.
- Field cells: **2204** (116 x 19). unknown 1221, high 371, medium 321, low 291; **61** carry `conditional: true`.

## Inputs and rules

- **sourceEvidence**: 5cbfb905-restOfMajorsSources_3.json
- **reviewedConceptBaseline**: 77ec67a4-purdueprogramfitreview20260816.json
- **conceptVocabulary**: 0edc9baf-rankingpolicy4.ts
- **cardContract**: 3ef656be-coresupportingranking.ts
- **joinKey**: publicProgramId (display names were never used to join)
- **checksumRule**: source.contentChecksum is the reviewed sourceChecksum copied verbatim from the reviewed concept baseline; no checksum was computed or invented in this pass.

Preservation rule applied throughout: a reviewed concept assignment was changed only where the richer source record gives a clear, source-supported reason. Every deviation appears in the change ledger below with its prior reviewed state, its final state, the reason and the supporting evidence.

## Concept changes from the reviewed baseline

83 changes across 46 programs.

| Program | Concept | Change | Prior | Final | Reason |
| --- | --- | --- | --- | --- | --- |
| `purdue-wl:accounting` | `financial-statements` | added | absent | supporting | A substantial required curriculum block omitted by the minimized reviewed summary: the intermediate/advanced financial reporting and audit sequence, plus explicit program-description language about preparing and interpreting financial information. |
| `purdue-wl:accounting` | `budgets-costs-controls` | added | absent | supporting | A required two-course managerial/cost accounting sequence that the reviewed summary did not capture. |
| `purdue-wl:accounting` | `data-analysis` | added | absent | supporting | Required analytics coursework named in the curriculum; also aligns this card with the reviewed baseline's own treatment of data-analysis as supporting on the sibling Daniels majors (Finance, Supply Chain and Operations Management). |
| `purdue-wl:aeronautical-astronautical-engineering` | `mathematics` | added | absent | supporting | Four required mathematics courses beyond the First-Year Engineering calculus sequence, plus explicit program-description language; the reviewed baseline recorded only the single core concept for this program. |
| `purdue-wl:aeronautical-astronautical-engineering` | `physics` | added | absent | supporting | A required physics course plus explicit program-description language naming physics as a foundation. |
| `purdue-wl:aeronautical-astronautical-engineering` | `mechanics-physical-systems` | added | absent | supporting | A substantial required aeromechanics, fluids, dynamics and structures block that the minimized reviewed summary omitted. |
| `purdue-wl:aeronautical-astronautical-engineering` | `design-build-test` | added | absent | supporting | A required design sequence running from the sophomore introduction to the senior vehicle-design course. |
| `purdue-wl:aeronautical-astronautical-engineering` | `laboratory-work` | added | absent | supporting | Four required laboratory courses in the major, which the minimized reviewed summary omitted. |
| `purdue-wl:aeronautical-astronautical-engineering` | `software-programming` | added | absent | supporting | A required programming course in which every option is a programming course, plus explicit program-description language. |
| `purdue-wl:aeronautical-engineering-technology` | `research-discovery` | added | absent | supporting | A required two-course applied research sequence culminating in the program capstone, which the minimized reviewed summary did not capture. |
| `purdue-wl:agricultural-engineering` | `engineering-systems` | added | absent | supporting | A substantial required engineering design and systems block that the minimized reviewed summary omitted. |
| `purdue-wl:agricultural-engineering` | `design-build-test` | added | absent | supporting | A required design sequence culminating in a named capstone design course. |
| `purdue-wl:agricultural-engineering` | `mathematics` | added | absent | supporting | Four required mathematics courses beyond the First-Year Engineering sequence. |
| `purdue-wl:animation-and-visual-effects` | `civil-infrastructure` | removed | supporting | absent | The only basis for this concept is the program description's list of industries where animation is applied ('education, product and packaging, construction, healthcare and courtrooms'). The full required 39-credit major, the 15-credit CGT Entertainment Selectives and the 52-credit other-requirements block contain no construction or infrastructure content whatsoever, so the concept does not characterise the program. |
| `purdue-wl:aquatic-sciences` | `animals-wildlife` | added | absent | supporting | A substantial required vertebrate-biology block that the minimized reviewed summary omitted. |
| `purdue-wl:aviation-management` | `law-government-policy` | added | absent | supporting | A dedicated required law course plus required safety/regulatory coursework, which the minimized reviewed summary did not capture. |
| `purdue-wl:biological-engineering` | `engineering-systems` | added | absent | supporting | A substantial required engineering transport and process block that the minimized reviewed summary omitted. |
| `purdue-wl:biological-engineering` | `design-build-test` | added | absent | supporting | A required two-semester capstone design sequence that the minimized reviewed summary omitted. |
| `purdue-wl:biological-engineering` | `laboratory-work` | added | absent | supporting | Three required laboratory courses inside the major that the minimized reviewed summary omitted. |
| `purdue-wl:biomedical-engineering` | `laboratory-work` | added | absent | supporting | Five required laboratory courses in the major, a substantial block the minimized reviewed summary omitted. |
| `purdue-wl:biomedical-engineering` | `design-build-test` | added | absent | supporting | A required design sequence in which every path is a design course, plus explicit program-description language about engineering design projects. |
| `purdue-wl:biomedical-health-sciences` | `chemistry` | added | absent | supporting | A substantial required chemistry block in the shared 67-credit core that the minimized reviewed summary omitted. |
| `purdue-wl:biomedical-health-sciences` | `biology-living-systems` | added | absent | supporting | A substantial required biology block in the shared 67-credit core that the minimized reviewed summary omitted. |
| `purdue-wl:cell-molecular-and-developmental-biology` | `laboratory-work` | added | absent | supporting | The reviewed baseline records no laboratory concept, while the retrieved requirements show laboratory coursework required in both the Biology Core and the chemistry requirement, plus a Base Lab Requirement specific to Biology majors. |
| `purdue-wl:cell-molecular-and-developmental-biology` | `chemistry` | added | absent | supporting | A 17-credit chemistry requirement shared by Biological Sciences majors is documented in the retrieved requirements but is not represented in the reviewed baseline. |
| `purdue-wl:chemical-biology-and-biochemistry` | `laboratory-work` | added | absent | supporting | The reviewed baseline records chemistry and biology but no laboratory concept, while the retrieved requirements name a required biochemistry laboratory and a research capstone that itself fulfils the Base Lab Requirement. |
| `purdue-wl:chemical-engineering` | `design-build-test` | added | absent | supporting | Two required process-design courses form a block the minimized reviewed summary omitted. |
| `purdue-wl:chemistry` | `laboratory-work` | added | absent | supporting | The reviewed baseline for the general Chemistry major records no laboratory concept, although the sibling Biochemistry (Chemistry) and ACS-accredited majors both carry one and this plan requires 7-10 credits of laboratory coursework of its own. |
| `purdue-wl:civil-engineering` | `design-build-test` | added | absent | supporting | A required design sequence culminating in a Senior Design Capstone that the program description describes in detail; omitted by the minimized reviewed summary. |
| `purdue-wl:civil-engineering` | `laboratory-work` | added | absent | supporting | A required hydraulics laboratory plus an explicit program-description statement that instructional laboratories run through the sophomore and junior years. |
| `purdue-wl:cybersecurity` | `law-government-policy` | added | absent | supporting | Two required courses place law, ethics and criminology inside the major, a block the minimized reviewed summary did not capture. |
| `purdue-wl:ecology-evolution-and-environmental-sciences` | `laboratory-work` | added | absent | supporting | The reviewed baseline records no laboratory concept, while the retrieved requirements name a dedicated ecology laboratory as this major's Base Lab Requirement on top of the shared biology and chemistry laboratories. |
| `purdue-wl:ecology-evolution-and-environmental-sciences` | `chemistry` | added | absent | supporting | A 17-credit chemistry requirement shared by Biological Sciences majors is documented in the retrieved requirements but is not represented in the reviewed baseline. |
| `purdue-wl:electrical-engineering` | `laboratory-work` | added | absent | supporting | An explicit required minimum of three Advanced-Level Laboratory courses inside the Electrical Engineering Electives block, plus two required fundamentals laboratories; a substantial block the minimized reviewed summary omitted. |
| `purdue-wl:elementary-education` | `psychology-behavior` | added | absent | supporting | The reviewed baseline records teaching-learning, clinical-patient-care and children-families but no psychology concept, while the retrieved required-course list contains a required EDPS learning-and-behaviour sequence that is not reducible to pedagogy. |
| `purdue-wl:english` | `history-culture-society` | added | absent | supporting | A required 3-credit Area B Multiethnic Studies course, shared by all three concentrations, that the minimized reviewed summary did not capture. |
| `purdue-wl:english-education` | `psychology-behavior` | added | absent | supporting | Reviewed baseline captures the English content and teaching axes but not the required educational-psychology sequence documented in the retrieved course list. |
| `purdue-wl:english-education` | `history-culture-society` | added | absent | supporting | The reviewed baseline records writing-language and communication-media but not the required literature/culture content, which the retrieved requirement blocks show is a substantial required share of the degree. |
| `purdue-wl:environmental-geosciences` | `laboratory-work` | added | absent | supporting | The reviewed baseline records no laboratory concept, while the retrieved requirements name a required engineering laboratory course, a required mineralogy course and an 8-10 credit laboratory science block. |
| `purdue-wl:finance` | `accounting-records` | added | absent | supporting | Three required accounting courses form a substantial block the minimized reviewed summary did not capture; the reviewed baseline already recognises the downstream financial-statements concept for this program. |
| `purdue-wl:finance` | `business-organizations` | added | absent | supporting | A full required business core spanning marketing, operations, strategy, information systems and organizational behavior, matching the reviewed baseline's own treatment of business-organizations as supporting on the sibling Daniels majors Accounting and Supply Chain and Operations Management. |
| `purdue-wl:food-science` | `manufacturing-production` | added | absent | supporting | A substantial required food-processing block that the minimized reviewed summary omitted. |
| `purdue-wl:food-science` | `laboratory-work` | added | absent | supporting | Five required laboratory courses inside the major that the minimized reviewed summary omitted. |
| `purdue-wl:forestry` | `plants-agriculture` | added | absent | supporting | A substantial required tree- and plant-biology block that the minimized reviewed summary omitted. |
| `purdue-wl:general-education-curriculum-and-instruction-non-licensure` | `psychology-behavior` | added | absent | supporting | The reviewed baseline captures teaching-learning, mathematics, writing-language and leadership-teamwork but not the required educational-psychology courses shown in the retrieved 16-credit required block. |
| `purdue-wl:general-education-educational-studies-non-licensure` | `psychology-behavior` | added | absent | supporting | The reviewed baseline captures teaching-learning, mathematics, research-discovery and children-families, but the retrieved major block is largely EDPS coursework in learning, cognition and counselling. |
| `purdue-wl:general-education-educational-studies-non-licensure` | `leadership-teamwork` | added | absent | supporting | Two required collaborative-leadership courses appear in the retrieved major block and are not represented in the reviewed baseline. |
| `purdue-wl:geology-and-geophysics` | `laboratory-work` | added | absent | supporting | The reviewed baseline records no laboratory concept, while the retrieved requirements name earth-materials coursework and an 8-credit physics laboratory science block. |
| `purdue-wl:health-and-disease` | `laboratory-work` | added | absent | supporting | The reviewed baseline records no laboratory concept, while the retrieved requirements name a required microbiology laboratory as this major's Base Lab Requirement on top of the shared biology and chemistry laboratories. |
| `purdue-wl:health-and-disease` | `chemistry` | added | absent | supporting | A 17-credit chemistry requirement shared by Biological Sciences majors is documented in the retrieved requirements but is not represented in the reviewed baseline. |
| `purdue-wl:inclusion-dual-license-special-and-elementary-education` | `psychology-behavior` | added | absent | supporting | The reviewed baseline records only teaching-learning and data-analysis; the retrieved 100-credit requirement block contains the same required educational-psychology and behaviour sequence recognised elsewhere in the college. |
| `purdue-wl:inclusion-dual-license-special-and-elementary-education` | `children-families` | added | absent | supporting | The dual K-6 / special-education licence scope and a required human-development course were not reflected in the reviewed baseline. |
| `purdue-wl:inclusion-dual-license-special-and-elementary-education` | `mathematics` | added | absent | supporting | Unlike the other licensure programs in this college, Inclusion requires a three-course mathematics content sequence, which the reviewed baseline did not capture. |
| `purdue-wl:interdisciplinary-studies` | `history-culture-society` | relationship_changed | supporting | core | The reviewed baseline recorded seven supporting concepts and NO core concept for this program, which would leave the card permanently unrankable (the candidate ranker excludes any card with zero matched core concepts). The program's own description is dominated by culture-and-society content, making history-culture-society the defining concept. |
| `purdue-wl:interior-design` | `buildings-built-environment` | added | absent | supporting | A substantial required block of built-environment coursework that the minimized reviewed summary omitted. |
| `purdue-wl:materials-engineering` | `laboratory-work` | added | absent | supporting | Three required 3-credit laboratory courses in the major, a substantial block the minimized reviewed summary omitted. |
| `purdue-wl:materials-engineering` | `design-build-test` | added | absent | supporting | A required three-course processing and design sequence that the minimized reviewed summary omitted. |
| `purdue-wl:neurobiology-and-physiology` | `laboratory-work` | added | absent | supporting | The reviewed baseline records no laboratory concept, while the retrieved requirements name a Base Lab Requirement of 1-4 credits alongside the shared biology and chemistry laboratories. |
| `purdue-wl:nuclear-engineering` | `laboratory-work` | added | absent | supporting | Four required laboratory courses totalling 10 credits, a substantial block the minimized reviewed summary omitted. |
| `purdue-wl:nuclear-engineering` | `physics` | added | absent | supporting | Two required nuclear-physics courses plus a required university physics course. |
| `purdue-wl:nuclear-engineering` | `materials` | added | absent | supporting | A required materials block including a dedicated 3-credit materials laboratory. |
| `purdue-wl:nuclear-engineering` | `mathematics` | added | absent | supporting | Four required mathematics courses beyond the First-Year Engineering calculus sequence. |
| `purdue-wl:nuclear-engineering` | `design-build-test` | added | absent | supporting | A required two-part senior design sequence that the minimized reviewed summary omitted. |
| `purdue-wl:nutrition-dietetics-nutrition-fitness-health` | `chemistry` | added | absent | supporting | The identical required chemistry block as the sibling Nutrition and Dietetics program appears in this double-major plan of study; the reviewed baseline recorded it for the sibling but not here. |
| `purdue-wl:nutrition-dietetics-nutrition-fitness-health` | `biology-living-systems` | added | absent | supporting | The identical required biology block as the sibling Nutrition and Dietetics program appears in this double-major plan of study. |
| `purdue-wl:occupational-environmental-health-sciences` | `chemistry` | added | absent | supporting | A substantial required chemistry block including analytical chemistry and biochemistry that the minimized reviewed summary omitted; the reviewed baseline carried no supporting concepts at all for this program. |
| `purdue-wl:occupational-environmental-health-sciences` | `biology-living-systems` | added | absent | supporting | A substantial required biology block that the minimized reviewed summary omitted. |
| `purdue-wl:occupational-environmental-health-sciences` | `laboratory-work` | added | absent | supporting | Required laboratory and instrumentation coursework that the minimized reviewed summary omitted. |
| `purdue-wl:occupational-environmental-health-sciences` | `law-government-policy` | added | absent | supporting | Two required environmental-policy requirements, one a named policy course, that the minimized reviewed summary omitted. |
| `purdue-wl:organizational-leadership` | `teaching-learning` | added | absent | supporting | Two required courses place instruction and developmental coaching inside the major, a block the minimized reviewed summary did not capture. |
| `purdue-wl:organizational-leadership` | `psychology-behavior` | added | absent | supporting | Two required psychology courses, one of them an industrial-organizational psychology course beyond the University Core, form a block the minimized reviewed summary did not capture. |
| `purdue-wl:pharmaceutical-sciences` | `research-discovery` | added | absent | supporting | A substantial required research block that the minimized reviewed summary omitted: PHSC 40000 Research Methods & Pharmacokinetics plus the required two-semester PHSC 46000/46100 Drug Discovery & Development sequence, reinforced by explicit program-description language about research careers. |
| `purdue-wl:pharmaceutical-sciences` | `laboratory-work` | added | absent | supporting | Two dedicated required laboratory courses appear in the plan of study; the reviewed baseline recorded chemistry and biology but not the laboratory environment. Consistent with the reviewed baseline's own treatment of laboratory-work as supporting on comparable chemistry programs. |
| `purdue-wl:physics-applied` | `laboratory-work` | added | absent | supporting | The reviewed baseline records no laboratory concept, while two dedicated laboratory courses are required inside the 41-42 credit major. |
| `purdue-wl:radiological-health-sciences` | `laboratory-work` | added | absent | supporting | Two required laboratory courses in the shared 61-credit core that the minimized reviewed summary omitted. |
| `purdue-wl:sales-and-marketing` | `economics-policy` | added | absent | supporting | A substantial required agricultural-economics block that the minimized reviewed summary omitted. |
| `purdue-wl:sales-and-marketing` | `data-analysis` | added | absent | supporting | Required analytics and econometrics coursework that the minimized reviewed summary omitted. |
| `purdue-wl:special-education-mild-intense-intervention-p-12` | `psychology-behavior` | added | absent | supporting | The reviewed baseline records only teaching-learning, data-analysis and helping-community, while the retrieved 91-credit requirement block is built on a required educational-psychology and behaviour-analysis sequence. |
| `purdue-wl:special-education-mild-intense-intervention-p-12` | `children-families` | added | absent | supporting | The programme is P-12 and the retrieved requirement block adds two required human-development courses outside the education prefixes, which the reviewed baseline did not capture. |
| `purdue-wl:studio-arts-and-technology` | `history-culture-society` | added | absent | supporting | A required 6-credit art history block that the minimized reviewed summary did not capture; the reviewed baseline recorded only one supporting concept for this program. |
| `purdue-wl:supply-chain-and-operations-management` | `economics-policy` | added | absent | supporting | Two required economics courses, one of them beyond the University Core, form a block the minimized reviewed summary did not capture. |
| `purdue-wl:theatre` | `history-culture-society` | added | absent | supporting | A required two-course theatre history and historiography block that the minimized reviewed summary did not capture; the reviewed baseline recorded no supporting concepts for this program. |
| `purdue-wl:theatre` | `leadership-teamwork` | added | absent | supporting | The program description states team collaboration as a defining mode of the degree, reinforced by required production practicum courses. |

Supporting evidence for each row is carried verbatim in `restOfMajorsClaude.audit.json` under `conceptAdjudication.changes[].supportingEvidence`, together with the source URL and locator.

## Field value distribution

| Field | high | medium | low | unknown | absent |
| --- | --- | --- | --- | --- | --- |
| `quantitative_intensity` | 32 | 37 | 10 | 37 | 0 |
| `statistics_data_intensity` | 4 | 25 | 51 | 36 | 0 |
| `computing_programming_intensity` | 9 | 19 | 41 | 47 | 0 |
| `writing_communication_intensity` | 4 | 26 | 37 | 49 | 0 |
| `research_investigation` | 6 | 17 | 13 | 80 | 0 |
| `theory_conceptual_analysis` | 67 | 41 | 0 | 8 | 0 |
| `applied_problem_solving` | 62 | 39 | 1 | 14 | 0 |
| `design_build` | 21 | 13 | 11 | 71 | 0 |
| `creative_production` | 11 | 2 | 7 | 96 | 0 |
| `laboratory_work` | 29 | 11 | 20 | 56 | 0 |
| `clinical_patient_facing` | 2 | 3 | 3 | 108 | 0 |
| `field_outdoor` | 5 | 5 | 7 | 99 | 0 |
| `teaching_helping` | 13 | 6 | 1 | 96 | 0 |
| `business_organizational` | 14 | 12 | 21 | 69 | 0 |
| `policy_social_systems` | 4 | 17 | 28 | 67 | 0 |
| `project_based_learning` | 6 | 13 | 4 | 93 | 0 |
| `culminating_experience` | 49 | 12 | 0 | 55 | 0 |
| `experiential_practice` | 31 | 19 | 15 | 51 | 0 |
| `teamwork_collaboration` | 2 | 4 | 21 | 89 | 0 |

**1221 of 2204 field cells are `unknown`.** That is the honest shape of this dataset rather than a defect to be engineered away: the source is a course-requirement record, so fields that a plan of study simply does not speak to (clinical placement, field work, capstone structure, team structures) are recorded as unknown, and `absent` is never asserted from nonappearance. No field cell in the dataset carries `absent`.

## Cross-program consistency findings

### CPC-01 - cross-college

**Finding.** The College of Science plans carry a college-level Science Core (Composition & Presentation, Computing, Laboratory Science, Statistics, Team-Building and Collaboration) that is a genuine requirement but identical across all 21 Science programs.

**Resolution.** Recorded uniformly as 'low' with 'required' status and college-level evidence, and raised only where a program's own major courses go further. Rubric R3 was not applied to suppress it, because these are college requirements rather than University Core designations - but they are explicitly non-differentiating within the college, and the audit records that so a downstream ranker does not read the uniform lows as signal.

### CPC-02 - College of Education (7 programs)

**Finding.** Every Education program requires the EDPS learning-and-behaviour spine (EDPS 23500 Learning And Motivation plus behaviour-support or cognition coursework), yet only Social Studies Education carried a psychology-behavior concept in the reviewed baseline.

**Resolution.** psychology-behavior added at supporting to the other six Education programs and to Mathematics Education, each with its own course-level evidence. No existing baseline concept was disturbed.

### CPC-03 - College of Science - Biological Sciences and Chemistry plans

**Finding.** The reviewed baseline assigned a laboratory-work concept to some laboratory-heavy Science majors (Biochemistry (Chemistry), Chemistry (ACS), Planetary Sciences, Statistics with Mathematics Option) but not to others with equally explicit required laboratory courses.

**Resolution.** laboratory-work added at supporting to Cell Molecular And Developmental Biology, Chemical Biology And Biochemistry, Chemistry, Ecology Evolution And Environmental Sciences, Environmental Geosciences, Geology And Geophysics, Health And Disease, Neurobiology And Physiology and Applied Physics, each citing that program's own named laboratory requirement (its Base Lab Requirement, PHYS 34000/45000, EEE 36000, or the shared BIOL/CHM laboratories).

### CPC-04 - College of Science - Biological Sciences plans

**Finding.** The 17-credit chemistry requirement shared by all Biological Sciences majors was not represented as a chemistry concept on several of those majors.

**Resolution.** chemistry added at supporting to Cell Molecular And Developmental Biology, Ecology Evolution And Environmental Sciences and Health And Disease, citing the shared requirement block.

### CPC-05 - Multidisciplinary Engineering

**Finding.** The reviewed baseline's visual-design and music-sound-performance concepts derive from the Visual Design Engineering and Theatre Engineering concentrations, not from the parent program's required core.

**Resolution.** Both concepts preserved (the standard is preserve-unless-clear-evidence, and concentration coursework is real coursework for the students who take it) but tagged evidenceScope 'concentration-specific' in the concept ledger, and the corresponding fields left unknown so concentration content does not inflate the parent card.

### CPC-06 - Animal Sciences, Horticulture

**Finding.** Business-related concepts on these Agriculture programs rest on named concentrations rather than on the parent required sequence.

**Resolution.** Same treatment as CPC-05: concepts preserved with evidenceScope 'concentration-specific', business_organizational left unknown on the parent card.

### CPC-07 - Animation And Visual Effects

**Finding.** The reviewed baseline's civil-infrastructure concept traces only to an industry-application sentence ('education, product and packaging, construction, healthcare and courtrooms'); nothing in the 39-credit major or its selectives supports it.

**Resolution.** The single concept removal in this pass. Recorded in the change ledger with the exact prior state and the reason.

### CPC-08 - Interdisciplinary Studies

**Finding.** The reviewed baseline gave this program seven supporting concepts and no core concept, which would make its card permanently unrankable (rankValidatedAiMajors excludes any card with zero matched core concepts, reason 'zero_core_match').

**Resolution.** The single relationship change in this pass: history-culture-society promoted supporting to core, justified by the program description's named focus areas (American culture; Jewish life and history; The African Diaspora). Recorded in the change ledger.

### CPC-09 - all colleges

**Finding.** Optional internships, 'opportunities' to do research, and encouraged-but-not-required experiences appear throughout the source and would inflate experiential_practice and research_investigation if read as requirements.

**Resolution.** Recorded as low with requiredStatus 'optional' and conditional true, with the source's own hedging language quoted in the evidence statement. 61 field cells carry conditional true across the dataset.

### CPC-10 - all colleges

**Finding.** Several reviewed concepts have no corroboration anywhere in the richer source record (for example clinical-patient-care on Elementary Education and Social Studies Education, teaching-learning on Mathematics and Health And Disease, business-organizations on Planetary Sciences).

**Resolution.** Concepts preserved unchanged per the preservation rule, their ledger entries carry the 'carried unchanged' evidence note, and the corresponding field is left value 'unknown' with relevance 'unknown' rather than being marked probably_irrelevant - recording the tension instead of resolving it by fiat.

## Source integrity observations

### SRC-01 (observation - not a packaging blocker)

The frozen source file's top-level statusNote claims 'Astrophysics (Science) was substantially upgraded from description-only to a full semester-by-semester course sequence via a College of Science Program Progression Guide PDF', but the purdue-wl:astrophysics program record itself still carries collectionStatus 'PARTIAL -- description-only' and requiredCourseSequence {note: 'Not obtainable'}.

*Impact:* The Astrophysics card is built from the record, not the statusNote: 17 of its 19 fields are unknown. If the progression-guide data exists elsewhere, re-running this program against it would materially improve the card.

### SRC-02 (observation - the cards remain importable and rankable)

Two Science programs (Astrophysics, Biomolecular Design) are description-only because the Purdue acalog preview_program.php pages sit behind an AWS WAF bot challenge, confirmed by both direct curl and a headless Chromium session. Biomolecular Design's second description sentence is additionally flagged in the source as paraphrased rather than verbatim.

*Impact:* These two cards carry the weakest evidence in the dataset (17 and 16 unknown fields respectively) and every value they do carry has requiredStatus 'unknown'.

### SRC-03 (observation)

13 programs carry a PARTIAL source-collection status while the reviewed concept baseline marks 112 of those same programs 'complete'; conversely purdue-wl:interdisciplinary-studies is COMPLETE in the source but 'partial' in the reviewed baseline. 14 such mismatches exist.

*Impact:* None - the two fields measure different things (source-collection completeness versus concept-review coverage). Both are carried on every per-program audit row so the difference is visible rather than silently reconciled.

### SRC-04 (observation)

Four programs have no usable program-specific description prose: their programDescriptionEvidence entries are shared College of Science boilerplate, a college licensure statement, or the source collector's own note that no 'About the Program' prose was present.

*Impact:* source.statement is null on those four cards rather than carrying text that is not about the program.

### SRC-05 (observation)

Two Science programs (Chemistry - American Chemical Society, Statistics with Mathematics Option) and one Mathematics program had their source reads truncated partway through the generic College of Science Core section, and two Education programs (both non-licensure General Education majors) have unre-captured Pass/No Pass, Civics Literacy and Race/Ethnic/Cultural Diversity sections.

*Impact:* Values on those cards that rest on the college-level core pattern rather than on the program's own transcription say so in their evidence statements, and teamwork_collaboration is left unknown where the component was never transcribed.

### SRC-06 (observation)

The source records a naming discrepancy for purdue-wl:ecology-evolution-and-environmental-sciences: the inventory display name is 'Ecology, Evolution and Environmental Sciences' while the catalog heading reads 'Ecology, Evolution, and Environmental Biology, BS'.

*Impact:* None for joining - publicProgramId is the join key throughout and display names were never used to match records.

### SRC-07 (observation)

The source file has no per-program retrieval timestamp.

*Impact:* source.retrievedAt is the literal string 'unknown' on every card. This satisfies the importer's non-empty check without asserting a retrieval time that the source does not record.

## Status mismatches between the two inputs

The source file's `collectionStatus` and the reviewed baseline's `status` measure different things (source-collection completeness versus concept-review coverage). Both are carried on every per-program row rather than reconciled.

| Program | source collection | reviewed baseline |
| --- | --- | --- |
| `purdue-wl:veterinary-technology` | PARTIAL | complete |
| `purdue-wl:virtual-design-construction` | PARTIAL | complete |
| `purdue-wl:multidisciplinary-engineering` | PARTIAL | complete |
| `purdue-wl:biomedical-health-sciences` | PARTIAL | complete |
| `purdue-wl:design-studies` | PARTIAL | complete |
| `purdue-wl:english` | PARTIAL | complete |
| `purdue-wl:interdisciplinary-studies` | COMPLETE | partial |
| `purdue-wl:music` | PARTIAL | complete |
| `purdue-wl:studio-arts-and-technology` | PARTIAL | complete |
| `purdue-wl:animal-sciences` | PARTIAL | complete |
| `purdue-wl:biochemistry` | PARTIAL | complete |
| `purdue-wl:forestry` | PARTIAL | complete |
| `purdue-wl:astrophysics` | PARTIAL | complete |
| `purdue-wl:biomolecular-design` | PARTIAL | complete |

## Packaging validation

Checks run against the importer contract in `core-supporting-ranking.ts`:

- 64-hex lowercase contentChecksum
- non-empty source.url / locator / retrievedAt
- statement is string or null
- concept IDs inside CONTROLLED_PROGRAM_CONCEPTS
- relationship in {core, supporting}
- no duplicate concept per card
- exactly 19 characteristic fields
- field value / relevance / requiredStatus enums
- conditional is boolean
- every evidence ref has id and statement
- at least one core concept (rankValidatedAiMajors zero_core_match exclusion)

**0 blockers.** Every card carries at least one core concept, so no card is excluded by `rankValidatedAiMajors` with reason `zero_core_match`.

## Per-program summary

| Program | School | Source | Core concepts | Supporting | Unknown fields |
| --- | --- | --- | --- | --- | --- |
| `purdue-wl:accounting` | Daniels School of Business | COMPLETE | `accounting-records` | 5 | 11 |
| `purdue-wl:actuarial-science` | Science | COMPLETE | `finance-markets` | 4 | 9 |
| `purdue-wl:aeronautical-astronautical-engineering` | Engineering | COMPLETE | `aerospace-flight` | 6 | 9 |
| `purdue-wl:aeronautical-engineering-technology` | Purdue Polytechnic Institute | COMPLETE | `aerospace-flight` | 3 | 8 |
| `purdue-wl:agricultural-education` | Agriculture | COMPLETE | `teaching-learning` | 2 | 9 |
| `purdue-wl:agricultural-engineering` | Agriculture | COMPLETE | `plants-agriculture` | 6 | 8 |
| `purdue-wl:animal-sciences` | Agriculture | PARTIAL | `animals-wildlife`, `biology-living-systems` | 6 | 13 |
| `purdue-wl:animation-and-visual-effects` | Purdue Polytechnic Institute | COMPLETE | `music-sound-performance` | 4 | 9 |
| `purdue-wl:anthropology` | Liberal Arts | COMPLETE | `history-culture-society` | 3 | 13 |
| `purdue-wl:aquatic-sciences` | Agriculture | COMPLETE | `environment-sustainability` | 3 | 10 |
| `purdue-wl:artificial-intelligence` | Liberal Arts | COMPLETE | `artificial-intelligence` | 4 | 13 |
| `purdue-wl:artificial-intelligence-science` | Science | COMPLETE | `artificial-intelligence` | 6 | 11 |
| `purdue-wl:astrophysics` | Science | PARTIAL | `earth-space` | 3 | 17 |
| `purdue-wl:aviation-management` | Purdue Polytechnic Institute | COMPLETE | `aerospace-flight` | 3 | 10 |
| `purdue-wl:biochemistry` | Agriculture | PARTIAL | `chemistry` | 5 | 9 |
| `purdue-wl:biochemistry-chemistry` | Science | COMPLETE | `chemistry` | 6 | 10 |
| `purdue-wl:biological-engineering` | Agriculture | COMPLETE | `biology-living-systems` | 8 | 10 |
| `purdue-wl:biomedical-engineering` | Engineering | COMPLETE | `biology-living-systems` | 8 | 6 |
| `purdue-wl:biomedical-health-sciences` | Health and Human Sciences | PARTIAL | `health-disease` | 3 | 12 |
| `purdue-wl:biomolecular-design` | Science | PARTIAL | `biology-living-systems` | 6 | 16 |
| `purdue-wl:brain-and-behavioral-sciences` | Health and Human Sciences | COMPLETE | `psychology-behavior` | 5 | 11 |
| `purdue-wl:cell-molecular-and-developmental-biology` | Science | COMPLETE | `biology-living-systems` | 6 | 10 |
| `purdue-wl:chemical-biology-and-biochemistry` | Science | COMPLETE | `biology-living-systems`, `chemistry` | 4 | 9 |
| `purdue-wl:chemical-engineering` | Engineering | COMPLETE | `chemistry` | 8 | 12 |
| `purdue-wl:chemistry` | Science | COMPLETE | `chemistry` | 7 | 11 |
| `purdue-wl:chemistry-american-chemical-society` | Science | COMPLETE | `chemistry` | 4 | 10 |
| `purdue-wl:civil-engineering` | Engineering | COMPLETE | `civil-infrastructure` | 4 | 6 |
| `purdue-wl:computer-and-information-technology` | Purdue Polytechnic Institute | COMPLETE | `computing-systems` | 2 | 9 |
| `purdue-wl:computer-engineering` | Engineering | COMPLETE | `computing-systems` | 4 | 9 |
| `purdue-wl:computer-engineering-technology` | Purdue Polytechnic Institute | COMPLETE | `computing-systems` | 2 | 8 |
| `purdue-wl:construction-engineering` | Engineering | COMPLETE | `construction-delivery` | 3 | 7 |
| `purdue-wl:construction-management` | Purdue Polytechnic Institute | COMPLETE | `construction-delivery` | 2 | 7 |
| `purdue-wl:creative-writing` | Liberal Arts | COMPLETE | `writing-language` | 2 | 15 |
| `purdue-wl:crop-soil-agroecosystem-sciences` | Agriculture | COMPLETE | `plants-agriculture` | 3 | 19 |
| `purdue-wl:cybersecurity` | Purdue Polytechnic Institute | COMPLETE | `computing-systems` | 2 | 8 |
| `purdue-wl:design-and-construction-integration` | Purdue Polytechnic Institute | COMPLETE | `construction-delivery` | 3 | 8 |
| `purdue-wl:design-studies` | Liberal Arts | PARTIAL | `visual-design` | 5 | 13 |
| `purdue-wl:developmental-and-family-science` | Health and Human Sciences | COMPLETE | `children-families` | 5 | 10 |
| `purdue-wl:digital-criminology` | Liberal Arts | COMPLETE | `computing-systems`, `law-government-policy` | 1 | 12 |
| `purdue-wl:early-childhood-education-and-exceptional-needs` | Health and Human Sciences | COMPLETE | `teaching-learning` | 3 | 8 |
| `purdue-wl:ecology-evolution-and-environmental-sciences` | Science | COMPLETE | `environment-sustainability` | 6 | 9 |
| `purdue-wl:electrical-engineering` | Engineering | COMPLETE | `energy-systems` | 5 | 9 |
| `purdue-wl:electrical-engineering-technology` | Purdue Polytechnic Institute | COMPLETE | `energy-systems` | 4 | 8 |
| `purdue-wl:elementary-education` | Education | COMPLETE | `teaching-learning` | 3 | 9 |
| `purdue-wl:english` | Liberal Arts | PARTIAL | `writing-language` | 2 | 16 |
| `purdue-wl:english-education` | Education | COMPLETE | `teaching-learning`, `writing-language` | 3 | 10 |
| `purdue-wl:environmental-geosciences` | Science | COMPLETE | `environment-sustainability` | 8 | 7 |
| `purdue-wl:family-and-consumer-sciences-education` | Health and Human Sciences | COMPLETE | `children-families`, `teaching-learning` | 3 | 7 |
| `purdue-wl:film-and-video` | Liberal Arts | COMPLETE | `music-sound-performance` | 2 | 13 |
| `purdue-wl:finance` | Daniels School of Business | COMPLETE | `finance-markets` | 7 | 10 |
| `purdue-wl:financial-counseling-planning` | Health and Human Sciences | COMPLETE | `finance-markets` | 4 | 8 |
| `purdue-wl:flight-professional-flight-technology` | Purdue Polytechnic Institute | COMPLETE | `aerospace-flight` | 1 | 7 |
| `purdue-wl:food-science` | Agriculture | COMPLETE | `food-nutrition` | 6 | 9 |
| `purdue-wl:forestry` | Agriculture | PARTIAL | `environment-sustainability` | 3 | 10 |
| `purdue-wl:game-development` | Purdue Polytechnic Institute | COMPLETE | `software-programming` | 8 | 9 |
| `purdue-wl:general-education-curriculum-and-instruction-non-licensure` | Education | COMPLETE | `teaching-learning` | 4 | 9 |
| `purdue-wl:general-education-educational-studies-non-licensure` | Education | COMPLETE | `teaching-learning` | 5 | 8 |
| `purdue-wl:geology-and-geophysics` | Science | COMPLETE | `earth-space` | 8 | 9 |
| `purdue-wl:health-and-disease` | Science | COMPLETE | `health-disease` | 5 | 10 |
| `purdue-wl:history-of-science-technology-and-medicine` | Liberal Arts | COMPLETE | `history-culture-society` | 6 | 15 |
| `purdue-wl:horticulture` | Agriculture | COMPLETE | `plants-agriculture` | 6 | 13 |
| `purdue-wl:hospitality-and-tourism-management` | Health and Human Sciences | COMPLETE | `hospitality-events` | 4 | 10 |
| `purdue-wl:human-services` | Health and Human Sciences | COMPLETE | `helping-community` | 4 | 10 |
| `purdue-wl:inclusion-dual-license-special-and-elementary-education` | Education | COMPLETE | `teaching-learning` | 4 | 7 |
| `purdue-wl:industrial-engineering-technology` | Purdue Polytechnic Institute | COMPLETE | `manufacturing-production` | 6 | 8 |
| `purdue-wl:industrial-microbiology-and-biotechnology` | Agriculture | COMPLETE | `biology-living-systems` | 2 | 17 |
| `purdue-wl:insect-biology` | Agriculture | COMPLETE | `biology-living-systems` | 7 | 10 |
| `purdue-wl:integrated-studio-arts` | Liberal Arts | COMPLETE | `art-creative-practice` | 2 | 14 |
| `purdue-wl:interdisciplinary-performance` | Liberal Arts | COMPLETE | `music-sound-performance` | 1 | 11 |
| `purdue-wl:interdisciplinary-studies` | Liberal Arts | COMPLETE | `history-culture-society` | 6 | 19 |
| `purdue-wl:interior-design` | Liberal Arts | COMPLETE | `visual-design` | 2 | 11 |
| `purdue-wl:kinesiology` | Health and Human Sciences | COMPLETE | `health-disease` | 3 | 12 |
| `purdue-wl:linguistics` | Liberal Arts | COMPLETE | `writing-language` | 4 | 15 |
| `purdue-wl:materials-engineering` | Engineering | COMPLETE | `materials` | 7 | 12 |
| `purdue-wl:mathematics` | Science | COMPLETE | `mathematics` | 1 | 11 |
| `purdue-wl:mathematics-applied` | Science | COMPLETE | `mathematics` | 3 | 11 |
| `purdue-wl:mathematics-education` | Science | COMPLETE | `mathematics`, `teaching-learning` | 4 | 7 |
| `purdue-wl:mechanical-engineering-technology` | Purdue Polytechnic Institute | COMPLETE | `mechanics-physical-systems` | 4 | 9 |
| `purdue-wl:mechatronics-engineering-technology` | Purdue Polytechnic Institute | COMPLETE | `automation-robotics` | 2 | 9 |
| `purdue-wl:medical-laboratory-sciences` | Health and Human Sciences | COMPLETE | `health-disease`, `laboratory-work` | 5 | 10 |
| `purdue-wl:multidisciplinary-engineering` | Engineering | PARTIAL | `engineering-systems` | 5 | 10 |
| `purdue-wl:music` | Liberal Arts | PARTIAL | `music-sound-performance` | 1 | 13 |
| `purdue-wl:neurobiology-and-physiology` | Science | COMPLETE | `biology-living-systems` | 4 | 10 |
| `purdue-wl:nuclear-engineering` | Engineering | COMPLETE | `energy-systems` | 6 | 12 |
| `purdue-wl:nursing` | Health and Human Sciences | COMPLETE | `clinical-patient-care` | 3 | 9 |
| `purdue-wl:nutrition-dietetics` | Health and Human Sciences | COMPLETE | `food-nutrition` | 4 | 8 |
| `purdue-wl:nutrition-dietetics-nutrition-fitness-health` | Health and Human Sciences | COMPLETE | `food-nutrition`, `health-disease` | 3 | 8 |
| `purdue-wl:nutrition-science` | Health and Human Sciences | COMPLETE | `food-nutrition` | 4 | 11 |
| `purdue-wl:occupational-environmental-health-sciences` | Health and Human Sciences | COMPLETE | `environment-sustainability`, `health-disease` | 4 | 9 |
| `purdue-wl:organizational-leadership` | Purdue Polytechnic Institute | COMPLETE | `leadership-teamwork` | 4 | 8 |
| `purdue-wl:pharmaceutical-sciences` | Pharmacy | COMPLETE | `health-disease` | 6 | 8 |
| `purdue-wl:physics-applied` | Science | COMPLETE | `physics` | 6 | 9 |
| `purdue-wl:planetary-sciences` | Science | COMPLETE | `earth-space` | 6 | 10 |
| `purdue-wl:plant-science` | Agriculture | COMPLETE | `plants-agriculture` | 4 | 10 |
| `purdue-wl:public-health` | Health and Human Sciences | COMPLETE | `health-disease` | 4 | 7 |
| `purdue-wl:radiological-health-sciences` | Health and Human Sciences | COMPLETE | `health-disease` | 4 | 10 |
| `purdue-wl:sales-and-marketing` | Agriculture | COMPLETE | `sales-marketing` | 6 | 11 |
| `purdue-wl:selling-sales-management` | Health and Human Sciences | COMPLETE | `sales-marketing` | 3 | 9 |
| `purdue-wl:social-studies-education` | Education | COMPLETE | `teaching-learning` | 6 | 11 |
| `purdue-wl:sociology` | Liberal Arts | COMPLETE | `history-culture-society` | 5 | 14 |
| `purdue-wl:sound-for-the-performing-arts` | Liberal Arts | COMPLETE | `music-sound-performance` | 1 | 10 |
| `purdue-wl:special-education-mild-intense-intervention-p-12` | Education | COMPLETE | `teaching-learning` | 4 | 10 |
| `purdue-wl:speech-language-hearing-sciences` | Health and Human Sciences | COMPLETE | `writing-language` | 3 | 11 |
| `purdue-wl:statistics-applied` | Science | COMPLETE | `statistics` | 6 | 12 |
| `purdue-wl:statistics-with-mathematics-option` | Science | COMPLETE | `mathematics`, `statistics` | 4 | 12 |
| `purdue-wl:studio-arts-and-technology` | Liberal Arts | PARTIAL | `art-creative-practice` | 2 | 14 |
| `purdue-wl:supply-chain-and-operations-management` | Daniels School of Business | COMPLETE | `supply-chain-operations` | 5 | 11 |
| `purdue-wl:sustainable-food-and-farming-systems` | Agriculture | COMPLETE | `food-nutrition`, `plants-agriculture` | 3 | 9 |
| `purdue-wl:theatre` | Liberal Arts | COMPLETE | `music-sound-performance` | 2 | 12 |
| `purdue-wl:turf-management-and-science` | Agriculture | COMPLETE | `plants-agriculture` | 3 | 12 |
| `purdue-wl:unmanned-aerial-systems` | Purdue Polytechnic Institute | COMPLETE | `aerospace-flight` | 3 | 10 |
| `purdue-wl:veterinary-technology` | Veterinary Medicine | PARTIAL | `animals-wildlife` | 3 | 16 |
| `purdue-wl:virtual-design-construction` | Purdue Polytechnic Institute | PARTIAL | `construction-delivery` | 3 | 14 |
| `purdue-wl:visual-communication-design` | Liberal Arts | COMPLETE | `communication-media`, `visual-design` | 2 | 10 |
| `purdue-wl:wildlife` | Agriculture | COMPLETE | `animals-wildlife` | 3 | 10 |
| `purdue-wl:world-languages-and-cultures` | Liberal Arts | COMPLETE | `history-culture-society`, `writing-language` | 4 | 18 |

Per-program review notes - what was deliberately left unknown and why, which concentrations were held out of the parent card, and which source gaps remain open - are in `restOfMajorsClaude.audit.json` under `perProgram[].reviewNote`.
