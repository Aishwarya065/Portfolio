import heapq
from collections import Counter, defaultdict

# A class to represent a node in the Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Defining a less-than method to make Node objects comparable in heapq
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman Tree
def build_huffman_tree(text):
    # Calculate frequency of each character in the text
    frequency = Counter(text)

    # Create a priority queue with all nodes
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    # Combine nodes until there is only one node left (root of the Huffman Tree)
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        # Merge two nodes to create a new internal node with combined frequency
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0]  # Return the root of the Huffman Tree

# Function to generate Huffman codes from the tree
def generate_codes(node, prefix='', codebook=None):
    if codebook is None:
        codebook = {}  # Initialize codebook as an empty dictionary

    if node is not None:
        # If this node is a leaf node, add its code to the codebook
        if node.char is not None:
            codebook[node.char] = prefix
        # Recurse on left and right children
        generate_codes(node.left, prefix + '0', codebook)
        generate_codes(node.right, prefix + '1', codebook)

    return codebook

# Function to encode the text using the Huffman codes
def encode_text(text, codebook):
    return ''.join(codebook[char] for char in text)

# Function to decode the encoded text back to original text
def decode_text(encoded_text, root):
    decoded_text = []
    current_node = root

    for bit in encoded_text:
        # Traverse the Huffman Tree
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        # If we reach a leaf node, append the character and reset to root
        if current_node.char is not None:
            decoded_text.append(current_node.char)
            current_node = root

    return ''.join(decoded_text)

# Main function to demonstrate Huffman Coding
def main():
    text = "this is an example for huffman encoding"

    print(f"Original text: {text}")

    # Build Huffman Tree
    root = build_huffman_tree(text)

    # Generate Huffman Codes
    codebook = generate_codes(root)
    print(f"Huffman Codes: {codebook}")

    # Encode the text
    encoded_text = encode_text(text, codebook)
    print(f"Encoded text: {encoded_text}")

    # Decode the text
    decoded_text = decode_text(encoded_text, root)
    print(f"Decoded text: {decoded_text}")

if __name__ == "__main__":
    main()
