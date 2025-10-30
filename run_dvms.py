import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from tidy_dvms import DVMS


client = DVMS(
    season=2023,                                # e.g., 2020–2025
    competition_name="EFL Championship",  # "English Premier League", "EFL Championship", "EFL Cup", "FA Cup"
    username="",
    password="",
)

# 1) Fixtures (choose representation)
fixtures_df   = client.fixtures(format="dataframe")  # Pandas DataFrame
fixtures_json = client.fixtures(format="json")       # list[dict]

# 2) Choose a match and compute outputs
# physical splits

opta_match_id = 2370657

players_splits = client.splits(opta_match_id=opta_match_id, type="players", model_form="denormalized")
teams_splits   = client.splits(opta_match_id=opta_match_id, type="teams", model_form="denormalized")
physical_summary = client.summary(opta_match_id=opta_match_id, model_form="denormalized")

print(players_splits)