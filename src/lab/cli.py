import argparse
import importlib

def load_case_module(case_id: str):
    """
    Turn [case_id] into 'lab.[case_id] and import it.
    """
    if not case_id.isdigit():
        raise ValueError(f"Case id must be numeric, got: {case_id}")
    
    module_name = f"lab.case_{case_id}"

    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError as e:
        raise ValueError(f"No case found for id: {case_id}") from e
    

def generate_case(case_id: str) -> None:
    case_module = load_case_module(case_id)

    if not hasattr(case_module, "generate"):
        raise ValueError(f"Case {case_id} does not define a generate() function")
    
    case_module.generate()


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="lab",
        description="Agent Investigation Lab CLI",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    generate_parser = subparsers.add_parser(
        "generate",
        help="Generate an investigation case",
    )
    
    generate_parser.add_argument(
        "case_id",
        help="Case id to generate, for example: 001"
    )

    args = parser.parse_args()

    if args.command == "generate":
        generate_case(args.case_id)

    else:
        parser.error(f"Unknown command: {args.command}")