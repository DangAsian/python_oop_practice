import cssutils as cu
import logging

cu.log.setLevel(logging.CRITICAL)
inbound_file = cu.parseFile("main.css", encoding=None)
print(inbound_file)

# inbound_file = cu.parseFile('main.css')

for rule in inbound_file.cssRules:
    if rule.type == rule.STYLE_RULE:
        for property in rule.style:
            print(property)


outbound_file = open("new_main.css","w")
