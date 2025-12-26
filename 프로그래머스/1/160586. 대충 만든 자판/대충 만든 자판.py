def solution(keymap, targets):
    ans = [0 for i in range(len(targets))]
    hash_keymap = {}
    for keys in keymap:
        for idx, key in enumerate(keys):
            if key not in hash_keymap:
                hash_keymap[key] = idx+1
            else:
                if hash_keymap[key] > idx+1:
                    hash_keymap[key] = idx+1 

    for idx, t in enumerate(targets):
        for ch in t:
            if ch in hash_keymap:
                ans[idx] += hash_keymap[ch]
            else:
                ans[idx] = -1
                break
    return ans