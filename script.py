import git
import os
from git_contributions_importer import *

mock_repo = git.Repo("/Users/taylor/Code/contributions-sync")

for d in next(os.walk("/Users/taylor/Code/bayphoto"))[1]:
    print("Starting directory:", d)
    repo = git.Repo("/Users/taylor/Code/bayphoto/" + d)
    importer = Importer([repo], mock_repo)
    importer.set_author(["taylorthurlow8@gmail.com", "taylor.thurlow@bayphoto.com"])
    importer.set_max_commits_per_day = [99999,99999]
    importer.set_start_from_last(True)
    importer.import_repository()



