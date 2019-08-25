import dictondisk
import pytest
import os

remove_keys = {0, (33, 12.23), "c", "中国"}

vanilla_dict = {
    0: 1337, 1: 3.14, 2: 2.71, 3: 1.61,
    "a": "Ą", "b": "✈!", "c": "東京", "中国": "共産",
    (1, .5): "lorem", (33, 12.23): "ipsum",
    -1: ["one", "two", "three"]
}

def test_contains_update():
    t = dictondisk.DictOnDisk(vanilla_dict)

    for i in vanilla_dict:
        assert i in t

def test_del():
    t = dictondisk.DictOnDisk(vanilla_dict)

    folder_name = t.folder.name

    del t

    assert not os.path.exists(folder_name)

def test_len():
    t = dictondisk.DictOnDisk(vanilla_dict)
    assert len(t) == len(vanilla_dict)

def test_getsetitem():
    t = dictondisk.DictOnDisk(vanilla_dict)

    for k, v in vanilla_dict.items():
        assert t[k] == v

    t[0] = 7331
    t[-1] = ["three", "two", "one"]

    assert t[0] == 7331
    assert t[-1] == ["three", "two", "one"]

    with pytest.raises(KeyError):
        u = t["0"]

def test_delitem():
    t = dictondisk.DictOnDisk(vanilla_dict)

    for i in remove_keys:
        del t[i]

    for k in vanilla_dict:

        if k in remove_keys:
            assert k not in t

        else:
            assert k in t

    with pytest.raises(KeyError):
        del t["0"]

def test_iter():
    t = dictondisk.DictOnDisk(vanilla_dict)

    all_keys = set(vanilla_dict.keys())

    for k in t:

        all_keys.remove(k)

    assert len(all_keys) == 0

def test_get():

    t = dictondisk.DictOnDisk(vanilla_dict)

    assert t.get(0) == 1337
    assert t.get((1, .5), "nice") == "lorem"

    assert t.get(52566) == None
    assert t.get(-2, "VΣЯY ПIᄃΣ") == "VΣЯY ПIᄃΣ"

def test_view_keys():
    pass

def test_view_values():
    pass

def test_view_items():
    pass
