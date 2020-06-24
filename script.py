import git
import os
from git_contributions_importer import *

mock_repo = git.Repo("/Users/taylorthurlow/Code/contributions-sync")

for d in next(os.walk("/Users/taylorthurlow/Code/bayphoto"))[1]:
    print("Starting directory:", d)
    repo = git.Repo("/Users/taylorthurlow/Code/bayphoto/" + d)
    importer = Importer([repo], mock_repo)
    importer.set_author([
        "taylorthurlow8@gmail.com",
        "taylor.thurlow@bayphoto.com",
        "taylorthurlow@me.com",
        "tthurlow@hey.com",
    ])
    importer.set_max_commits_per_day([99999,99999])
    importer.set_start_from_last(False)
    importer.set_max_changes_per_file(10000)
    importer.set_collapse_multiple_changes_to_one(False)
    importer.import_repository()



