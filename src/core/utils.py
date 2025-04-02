from typing import List, Dict
from pathlib import Path


def summarize_clusters(clusters: List[Dict]) -> None:
    cluster_sizes = [len(c["files"]) for c in clusters]

    print("\n📊 Match Summary:")
    print(f"  • Clusters: {len(clusters)}")

    name_like = sum(len(c.get("reasons", {}).get("name_match", [])) for c in clusters)
    size_like = sum(len(c.get("reasons", {}).get("size_match", [])) for c in clusters)
    meta_like = sum(len(c.get("reasons", {}).get("meta_match", [])) for c in clusters)

    print(f"  • Match Types → Name: {name_like} | Size: {size_like} | Meta: {meta_like}")
    print(f"  • Cluster Size → Min: {min(cluster_sizes)} | Max: {max(cluster_sizes)} | Avg: {sum(cluster_sizes)/len(cluster_sizes):.2f}")

    top_clusters = sorted(clusters, key=lambda c: len(c["files"]), reverse=True)[:3]
    print("\n🔥 Largest Clusters:")
    for i, cluster in enumerate(top_clusters, 1):
        preview = ", ".join(cluster["files"][:3])
        if len(cluster["files"]) > 3:
            preview += "…"
        print(f"  {i}. {len(cluster['files'])} files → [{preview}]")


def clean_cluster_output(match_clusters: List[Dict], root_dir: Path, show_relative_paths: bool) -> List[Dict]:
    def safe_stringify(obj):
        if isinstance(obj, Path):
            return str(obj.relative_to(root_dir) if show_relative_paths else obj)
        elif isinstance(obj, dict):
            return {safe_stringify(k): safe_stringify(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [safe_stringify(i) for i in obj]
        else:
            return obj

    cleaned = []
    for cluster in match_clusters:
        cleaned_cluster = {
            "files": [safe_stringify(f) for f in cluster["files"]],
            "weight": cluster["weight"]
        }
        if "why" in cluster:
            cleaned_cluster["why"] = safe_stringify(cluster["why"])
        cleaned.append(cleaned_cluster)

    return cleaned