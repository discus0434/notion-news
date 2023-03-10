import os

from dotenv import load_dotenv

load_dotenv()

########################################################################
# Notion
########################################################################
# ID of the database to archive
DATABASE_ID = os.getenv("DATABASE_ID")
# Access token of the integration (https://www.notion.so/my-integrations)
NOTION_ACCESS_TOKEN = os.getenv("NOTION_ACCESS_TOKEN")

########################################################################
# Twitter
########################################################################
# Twitter API keys (https://developer.twitter.com/en/portal/dashboard)
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_TOKEN_SECRET = os.getenv("TWITTER_TOKEN_SECRET")


ARXIV_CATEGORIES = {
    "acc-phys": "accelerator physics",
    "adap-org": "adaptation, noise, and self-organizing systems",
    "alg-geom": "algebraic geometry",
    "ao-sci": "atmospheric-oceanic sciences",
    "astro-ph": "astrophysics",
    "astro-ph.CO": "cosmology and nongalactic astrophysics",
    "astro-ph.EP": "earth and planetary astrophysics",
    "astro-ph.GA": "astrophysics of galaxies",
    "astro-ph.HE": "high energy astrophysical phenomena",
    "astro-ph.IM": "instrumentation and methods for astrophysics",
    "astro-ph.SR": "solar and stellar astrophysics",
    "atom-ph": "atomic, molecular and optical physics",
    "bayes-an": "bayesian analysis",
    "chao-dyn": "chaotic dynamics",
    "chem-ph": "chemical physics",
    "cmp-lg": "computation and language",
    "comp-gas": "cellular automata and lattice gases",
    "cond-mat": "condensed matter",
    "cond-mat.dis-nn": "disordered systems and neural networks",
    "cond-mat.mes-hall": "mesoscale and nanoscale physics",
    "cond-mat.mtrl-sci": "materials science",
    "cond-mat.other": "other condensed matter",
    "cond-mat.quant-gas": "quantum gases",
    "cond-mat.soft": "soft condensed matter",
    "cond-mat.stat-mech": "statistical mechanics",
    "cond-mat.str-el": "strongly correlated electrons",
    "cond-mat.supr-con": "superconductivity",
    "cs.AI": "artificial intelligence",
    "cs.AR": "hardware architecture",
    "cs.CC": "computational complexity",
    "cs.CE": "computational engineering, finance, and science",
    "cs.CG": "computational geometry",
    "cs.CL": "computation and language",
    "cs.CR": "cryptography and security",
    "cs.CV": "computer vision and pattern recognition",
    "cs.CY": "computers and society",
    "cs.DB": "databases",
    "cs.DC": "distributed, parallel, and cluster computing",
    "cs.DL": "digital libraries",
    "cs.DM": "discrete mathematics",
    "cs.DS": "data structures and algorithms",
    "cs.ET": "emerging technologies",
    "cs.FL": "formal languages and automata theory",
    "cs.GL": "general literature",
    "cs.GR": "graphics",
    "cs.GT": "computer science and game theory",
    "cs.HC": "human-computer interaction",
    "cs.IR": "information retrieval",
    "cs.IT": "information theory",
    "cs.LG": "machine learning",
    "cs.LO": "logic in computer science",
    "cs.MA": "multiagent systems",
    "cs.MM": "multimedia",
    "cs.MS": "mathematical software",
    "cs.NA": "numerical analysis",
    "cs.NE": "neural and evolutionary computing",
    "cs.NI": "networking and internet architecture",
    "cs.OH": "other computer science",
    "cs.OS": "operating systems",
    "cs.PF": "performance",
    "cs.PL": "programming languages",
    "cs.RO": "robotics",
    "cs.SC": "symbolic computation",
    "cs.SD": "sound",
    "cs.SE": "software engineering",
    "cs.SI": "social and information networks",
    "cs.SY": "systems and control",
    "dg-ga": "differential geometry",
    "econ.EM": "econometrics",
    "econ.GN": "general economics",
    "econ.TH": "theoretical economics",
    "eess.AS": "audio and speech processing",
    "eess.IV": "image and video processing",
    "eess.SP": "signal processing",
    "eess.SY": "systems and control",
    "funct-an": "functional analysis",
    "gr-qc": "general relativity and quantum cosmology",
    "hep-ex": "high energy physics - experiment",
    "hep-lat": "high energy physics - lattice",
    "hep-ph": "high energy physics - phenomenology",
    "hep-th": "high energy physics - theory",
    "math-ph": "mathematical physics",
    "math.AC": "commutative algebra",
    "math.AG": "algebraic geometry",
    "math.AP": "analysis of pdes",
    "math.AT": "algebraic topology",
    "math.CA": "classical analysis and odes",
    "math.CO": "combinatorics",
    "math.CT": "category theory",
    "math.CV": "complex variables",
    "math.DG": "differential geometry",
    "math.DS": "dynamical systems",
    "math.FA": "functional analysis",
    "math.GM": "general mathematics",
    "math.GN": "general topology",
    "math.GR": "group theory",
    "math.GT": "geometric topology",
    "math.HO": "history and overview",
    "math.IT": "information theory",
    "math.KT": "k-theory and homology",
    "math.LO": "logic",
    "math.MG": "metric geometry",
    "math.MP": "mathematical physics",
    "math.NA": "numerical analysis",
    "math.NT": "number theory",
    "math.OA": "operator algebras",
    "math.OC": "optimization and control",
    "math.PR": "probability",
    "math.QA": "quantum algebra",
    "math.RA": "rings and algebras",
    "math.RT": "representation theory",
    "math.SG": "symplectic geometry",
    "math.SP": "spectral theory",
    "math.ST": "statistics theory",
    "mtrl-th": "materials theory",
    "nlin.AO": "adaptation and self-organizing systems",
    "nlin.CD": "chaotic dynamics",
    "nlin.CG": "cellular automata and lattice gases",
    "nlin.PS": "pattern formation and solitons",
    "nlin.SI": "exactly solvable and integrable systems",
    "nucl-ex": "nuclear experiment",
    "nucl-th": "nuclear theory",
    "patt-sol": "pattern formation and solitons",
    "physics.acc-ph": "accelerator physics",
    "physics.ao-ph": "atmospheric and oceanic physics",
    "physics.app-ph": "applied physics",
    "physics.atm-clus": "atomic and molecular clusters",
    "physics.atom-ph": "atomic physics",
    "physics.bio-ph": "biological physics",
    "physics.chem-ph": "chemical physics",
    "physics.class-ph": "classical physics",
    "physics.comp-ph": "computational physics",
    "physics.data-an": "data analysis, statistics and probability",
    "physics.ed-ph": "physics education",
    "physics.flu-dyn": "fluid dynamics",
    "physics.gen-ph": "general physics",
    "physics.geo-ph": "geophysics",
    "physics.hist-ph": "history and philosophy of physics",
    "physics.ins-det": "instrumentation and detectors",
    "physics.med-ph": "medical physics",
    "physics.optics": "optics",
    "physics.plasm-ph": "plasma physics",
    "physics.pop-ph": "popular physics",
    "physics.soc-ph": "physics and society",
    "physics.space-ph": "space physics",
    "plasm-ph": "plasma physics",
    "q-alg": "quantum algebra and topology",
    "q-bio": "quantitative biology",
    "q-bio.BM": "biomolecules",
    "q-bio.CB": "cell behavior",
    "q-bio.GN": "genomics",
    "q-bio.MN": "molecular networks",
    "q-bio.NC": "neurons and cognition",
    "q-bio.OT": "other quantitative biology",
    "q-bio.PE": "populations and evolution",
    "q-bio.QM": "quantitative methods",
    "q-bio.SC": "subcellular processes",
    "q-bio.TO": "tissues and organs",
    "q-fin.CP": "computational finance",
    "q-fin.EC": "economics",
    "q-fin.GN": "general finance",
    "q-fin.MF": "mathematical finance",
    "q-fin.PM": "portfolio management",
    "q-fin.PR": "pricing of securities",
    "q-fin.RM": "risk management",
    "q-fin.ST": "statistical finance",
    "q-fin.TR": "trading and market microstructure",
    "quant-ph": "quantum physics",
    "solv-int": "exactly solvable and integrable systems",
    "stat.AP": "applications",
    "stat.CO": "computation",
    "stat.ME": "methodology",
    "stat.ML": "machine learning",
    "stat.OT": "other statistics",
    "stat.TH": "statistics theory",
    "supr-con": "superconductivity",
    "test": "test",
    "test.dis-nn": "test disruptive networks",
    "test.mes-hall": "test hall",
    "test.mtrl-sci": "test mtrl-sci",
    "test.soft": "test soft",
    "test.stat-mech": "test mechanics",
    "test.str-el": "test electrons",
    "test.supr-con": "test superconductivity",
}
