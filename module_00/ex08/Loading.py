from time import time

def ft_tqdm(lst: range) -> None:
    start = time()
    total = len(lst)
    for i, item in enumerate(lst, start=1):
        progress = int(i / total * 100)
        bar_len = 50
        bar = "=" * int(progress / 2) + ">" + " " * (bar_len - int(progress / 2) - 1)
        elapsed = time() - start
        print(f"\r{progress:3d}%|[{bar}]| {i}/{total} | elapsed: {elapsed:5.2f}s", end='', flush=True)
        yield item
    print()
