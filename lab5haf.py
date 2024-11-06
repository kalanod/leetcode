from collections import Counter
import heapq

# Provided text
text = "четверть четверика гороха без червоточинки."

# Step 1: Calculate character frequencies
frequencies = Counter(text)


# Step 2: Build the Huffman tree
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Function to build Huffman tree
def build_huffman_tree(frequencies):
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]


# Function to generate Huffman codes
def generate_huffman_codes(root, code="", code_map={}):
    if root is not None:
        if root.char is not None:  # Leaf node
            code_map[root.char] = code
        generate_huffman_codes(root.left, code + "0", code_map)
        generate_huffman_codes(root.right, code + "1", code_map)
    return code_map


# Build the Huffman tree and generate codes
huffman_tree_root = build_huffman_tree(frequencies)
huffman_codes = generate_huffman_codes(huffman_tree_root)

# Step 3: Calculate the preamble size for regular Huffman encoding
# Generate detailed breakdown of code lengths
breakdown = " + ".join(f"{len(code)}" for code in huffman_codes.values())
preamble_size = sum(len(code) for code in huffman_codes.values())

# Output the result in specified format
print(f"Preamble size calculation: [{breakdown} = {preamble_size}]")
