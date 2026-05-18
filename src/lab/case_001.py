

from pathlib import Path

def create_case_skeleton(case_slug: str) -> Path:
    case_dir = Path("cases") / case_slug 

    observed_dir = case_dir / "observed"
    hidden_dir = case_dir / "hidden"
    runs_dir = case_dir / "runs"

    observed_dir.mkdir(parents=True, exist_ok=True)
    hidden_dir.mkdir(parents=True, exist_ok=True)
    runs_dir.mkdir(parents=True, exist_ok=True)

    # Observed files
    (observed_dir / "case_prompt.md").write_text(
        "# Case Prompt\n\nInvestigate what happened.\n",
        encoding="utf-8",
    )

    (observed_dir / "data_dictionary.md").write_text(
        "# Data Dictionary\n\nDescribe the observed datasets here.\n",
        encoding="utf-8",
    )

    (observed_dir / "customers.csv").write_text(
        "customer_id,name,segment\n",
        encoding="utf-8",
    )

    (observed_dir / "support_tickets.csv").write_text(
        "ticket_id,customer_id,created_date,category,severity\n",
        encoding="utf-8",
    )

    (observed_dir / "events.csv").write_text(
        "event_id,customer_id,event_date,event_type\n",
        encoding="utf-8",
    )

    # Hidden files
    (hidden_dir / "ground_truth.json").write_text(
        "{\n  \"true_cause\": null\n}\n",
        encoding="utf-8",
    )

    (hidden_dir / "rubric.json").write_text(
        "{\n  \"criteria\": []\n}\n",
        encoding="utf-8",
    )

    return case_dir




def generate() -> None:
    case_dir = create_case_skeleton("case_001_confound_churn")
    print(f"Generated case skeleton at: {case_dir}")

