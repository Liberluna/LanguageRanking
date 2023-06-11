import requests
from collections import Counter

print("(c) : Liberluna / amex / @macl2189")

def calc(org_name, access_token):
    url = f"https://api.github.com/orgs/{org_name}/repos"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {access_token}"
    }
    response = requests.get(url, headers=headers)
    repositories = response.json()
    repository_ranking = []
    for repo in repositories:
        languages = []
        repo_url = repo["languages_url"]
        repo_response = requests.get(repo_url, headers=headers)
        repo_data = repo_response.json()
        total_lines = sum(repo_data.values())
        language_ratios = {language: (count / total_lines) * 100 for language, count in repo_data.items()}
        repository_ranking.append((repo["name"], language_ratios))
    repository_ranking.sort(key=lambda x: sum(x[1].values()), reverse=True)
    return repository_ranking

org_name = "Liberluna"
#organizationの名前
access_token = "" 
#アクセストークン　取得手順は調べてください....

ranking = calc(org_name, access_token)

print(f"Organization: {org_name}")
print("Repository Language Usage Percentage")
print("----------------------------------")

all_rank = {
    
}
print("----------------------------------")
for repo, language_ratios in ranking:
    print(f"Repository: {repo}")
    for language, ratio in language_ratios.items():
        print(f"{language}: {ratio:.2f}%")
        if language not in all_rank:
            all_rank[language] = [
                
            ]
        all_rank[language].append(ratio * len(language_ratios.items()))
    print("----------------------------------")

print("Language Usage Ranking")
print("----------------------------------")
all_percentage = 0
for language, rank in all_rank.items():
    all_percentage += sum(rank) / len(rank)    

for language, rank in all_rank.items():
    all_rank[language] = sum(rank) / len(rank) / all_percentage * 100

#Sortする
all_rank = sorted(all_rank.items(), key=lambda x: x[1], reverse=True)

iters = 0
for language, percentage in all_rank:
    iters += 1
    print(f"{iters}. {language}: {percentage:.2f}%")

