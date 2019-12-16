from uuid import uuid4
from flask import Flask, jsonify, request

from com.freshman.blockchain.firstblock import Blockchain

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    """
    注册节点
    :return:
    """
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error:Please supply a valid list of nodes", 400
    for node in nodes:
        blockchain.register_node(node)
    response = {
        'message': "New nodes have been added",
        'total_nodes': list(blockchain.nodes)
    }
    return jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    """
    解决冲突
    :return:
    """
    replaced = blockchain.resolve_conflicts()
    if replaced:
        response = {
            'message': "Our chain was replaced",
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': "Our chain is authoritative",
            'chain': blockchain.chain
        }
    return jsonify(response), 200


@app.route('/mine', methods=['GET'])
def mine():
    """
    挖矿正是神奇所在，它很简单，做了一下三件事：
    1、计算工作量证明 PoW
    2、通过新增一个交易授予矿工（自己）一个币
    3、构造新区块并将其添加到链中
    :return:
    """
    # We run the proof of work algorithm to get the next proof...
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # 给工作量证明的节点提供奖励
    # 发送者为"0"表明是新挖出的币
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    # Forget the new Block by adding it to the chain
    block = blockchain.new_block(proof)

    response = {
        'message': 'New Block Forged',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

    # return "We'll mine a new Block"


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """
    处理一个交易
    :return:
    """
    values = request.get_json()
    # Check tha he required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return "Missing values", 400
    # Create a new Transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201
    # return "We'll add a new transaction"


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
