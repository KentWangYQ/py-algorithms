# -*- coding: utf-8 -*-

import copy
from hashlib import md5
from struct import unpack_from
from bisect import bisect_left


# 普通hash分布算法
def normal_hash(node_count, item_count):
    """
    普通hash分布算法

    取余分布
    在分布式系统中存在严重问题，新加入结点时，会造成绝大部分数据需要迁移
    :param node_count: 结点总数
    :param item_count: 数据总量
    :return:
    """
    node_item_count = [0] * node_count
    new_node_count = node_count + 1
    moved_item_count = 0

    for item in range(item_count):
        _hash = unpack_from('>I', md5(str(item).encode()).digest())[0]
        _id = _hash % node_count
        node_item_count[_id] += 1

        new_id = _hash % new_node_count
        moved_item_count += 0 if _id == new_id else 1

    avg_count = item_count / node_count
    print(f'Avg item count on node: {avg_count}')

    max_count = max(node_item_count)
    over_per = (max_count - avg_count) / avg_count * 100
    print(f'Most item node has {over_per:.2f}% over')

    min_count = min(node_item_count)
    under_per = (min_count - avg_count) / avg_count * 100
    print(f'Least item node has {under_per:.2f}% under')

    moved_per = moved_item_count / item_count * 100
    print(f'Item moved per after add one node: {moved_per:.2f}%')


# 一致性Hash算法
def consistent_hash(node_count, item_count):
    """
    一致性Hash算法

    步骤：
        1. 首先求出每个节点(机器名或者是IP地址)的哈希值，并将其分配到一个圆环区间上(这里取0-2^32).
        2. 求出需要存储对象的哈希值，也将其分配到这个圆环上.
        3. 从对象映射到的位置开始顺时针查找，将对象保存到找到的第一个节点上.
    优缺点：
        1. 优点：解决了不同hash算法在新结点加入时，需要大量迁移数据的问题。
        2. 缺点：结点数较少时，数据在结点上的数据分布不均
    :param node_count: 结点总数
    :param item_count: 数据总量
    :return:
    """
    nodes, nodes_new = [], []
    node_item_count = [0] * node_count
    moved_item_count = 0

    for node in range(node_count):
        _id = unpack_from('>I', md5(str(node).encode()).digest())[0]
        _idx = bisect_left(nodes, _id)
        nodes.insert(_idx, _id)
        nodes_new.insert(_idx, _id)

    _id = unpack_from('>I', md5(str(node_count).encode()).digest())[0]
    _idx = bisect_left(nodes_new, _id)
    nodes_new.insert(_idx, _id)

    for item in range(item_count):
        _id = unpack_from('>I', md5(str(item).encode()).digest())[0]
        _idx = bisect_left(nodes, _id) % node_count
        _idx_new = bisect_left(nodes_new, _id) % node_count

        node_item_count[_idx] += 1
        moved_item_count += 0 if _idx == _idx_new else 1

    avg_count = item_count / node_count
    print(f'Avg item count on node: {avg_count}')

    max_count = max(node_item_count)
    over_per = (max_count - avg_count) / avg_count * 100
    print(f'Most item node has {over_per:.2f}% over')

    min_count = min(node_item_count)
    under_per = (min_count - avg_count) / avg_count * 100
    print(f'Least item node has {under_per:.2f}% under')

    moved_per = moved_item_count / item_count * 100
    print(f'Item moved per after add one node: {moved_per:.2f}%')


# 一致性Hash算法(虚拟结点)
def consistent_hash_vnode(node_count, v, item_count):
    """
    一致性Hash算法(虚拟结点)

    在一致性Hash算法的基础上，增加虚拟结点支持
    一致性Hash算法的最主要问题是：结点数量较少时，数据在节点上分布不均匀，
    因此引入虚拟结点，每个结点分解为多个虚拟结点，使虚拟结点在环上分布更均匀，从而促使数据分布更均匀
    :param node_count: 结点总数
    :param v: 每个实体结点生成的虚拟结点数量
    :param item_count: 数据总量
    :return:
    """
    vnode_count, vnodes_count_new = node_count * v, (node_count + 1) * v
    nodes, nodes_new, vnodes, vnodes_new = [], [], [], []
    vnode_map, vnode_map_new = {}, {}
    node_item_count = [0] * node_count
    moved_item_count = 0

    # 创建实体结点和虚拟结点列表及两者mapping关系
    for node in range(node_count):
        node_id = unpack_from('>I', md5(str(node).encode()).digest())[0]
        node_idx = bisect_left(nodes, node_id)
        nodes.insert(node_idx, node_id)
        for i in range(v):
            vnode = node * v + i
            vnode_id = unpack_from('>I', md5(str(vnode).encode()).digest())[0]
            vnode_map[str(vnode_id)] = node_id

            vnode_idx = bisect_left(vnodes, vnode_id)
            vnodes.insert(vnode_idx, vnode_id)
            vnodes_new.insert(vnode_idx, vnode_id)

    # 追加一个实体结点
    node_id = unpack_from('>I', md5(str(node_count).encode()).digest())[0]
    node_idx = bisect_left(nodes, node_id)
    nodes_new = nodes[:]
    nodes_new.insert(node_idx, node_id)
    vnode_map_new = copy.deepcopy(vnode_map)
    # 为新的实体结点生成虚拟结点
    for i in range(v):
        vnode = node_count * v + i
        vnode_id = unpack_from('>I', md5(str(vnode).encode()).digest())[0]
        vnode_map_new[str(vnode_id)] = node_id
        vnode_idx = bisect_left(vnodes, vnode_id)
        vnodes_new.insert(vnode_idx, vnode_id)

    # 数据散布
    for item in range(item_count):
        _id = unpack_from('>I', md5(str(item).encode()).digest())[0]

        vnode_id = vnodes[bisect_left(vnodes, _id) % vnode_count]
        vnode_id_new = vnodes_new[bisect_left(vnodes_new, _id) % vnode_count]

        node_id = vnode_map.get(str(vnode_id))
        node_id_new = vnode_map_new.get(str(vnode_id_new))

        _idx_node = nodes.index(node_id)

        node_item_count[_idx_node] += 1
        moved_item_count += 0 if node_id == node_id_new else 1

    avg_count = item_count / node_count
    print(f'Avg item count on node: {avg_count}')

    max_count = max(node_item_count)
    over_per = (max_count - avg_count) / avg_count * 100
    print(f'Most item node has {over_per:.2f}% over')

    min_count = min(node_item_count)
    under_per = (min_count - avg_count) / avg_count * 100
    print(f'Least item node has {under_per:.2f}% under')

    moved_per = moved_item_count / item_count * 100
    print(f'Item moved per after add one node: {moved_per:.2f}%')
