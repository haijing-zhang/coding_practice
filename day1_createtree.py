
# input
data = [
    'software_wireless_integration',
    'software_wireless_protocol',
    'software_wireless_platform',
    'software_wireless_infra',
    'hardware_SoC_platform',
    'software_iOS_platform',
    'software_MacOS_integration',
    'software_AIML_infra',
    'software_AIML_Siri_integration',
'software_AIML_Vision_integration'
,
    'software_wireless_protocol',
    'hardware_SoC_platform',
    'hardware_RF_integration',
    'software_wireless_protocol',
    'software_iOS_integration'
]

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.count = 1
        self.floor = -1

root = TreeNode('root')
for item in data:
   curRoot = root
   words = item.split('_')
   for word in words:
      isfound = False
      for node in curRoot.children:
        if node.name == word:
           node.count += 1
           curRoot = node
           isfound = True
           break
      if not isfound:
        curNode = TreeNode(word)
        curNode.floor = curRoot.floor + 1
        curRoot.children.append(curNode)
        curRoot = curNode


#DFS print current tree
def traverse(node):
   for leaf in node.children:
      if not leaf: return
      if leaf.floor >= 0: print(leaf.floor * " " + f'{leaf.name} ({leaf.count})' )
      traverse(leaf)

      
traverse(root)

# output = 
# software (12)
#     wireless (6)
#         integration (1)
#         protocol (3)
#         platform (1)
#         infra (1)
#     iOS (2)
#         platform (1)
#         integration (1)
#     MacOS (1)
#         integration (1)
#     AIML (3)
#         infra (1)
#         Siri (1)
#             integration (1)
#         Vision (1)
#             integration (1)
# hardware (3)
#     SoC (2)
#         platform (2)
#     RF (1)
#         integration (1)


