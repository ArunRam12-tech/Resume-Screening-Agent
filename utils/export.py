import pandas as pd


def export_results(results):

    df = pd.DataFrame(results)

    df.insert(0, "Rank", range(1, len(df)+1))

    df.to_csv(
        "data/output/ranked_candidates.csv",
        index=False
    )

    print("\nCSV saved successfully!")