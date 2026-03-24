class Solution:
    def isValid(self, code: str) -> bool:
        n = len(code)
        i = 0
        tag_stack = []

        # Helper to check if a TAG_NAME is valid (Rule 3)
        def is_valid_tag_name(tag_name: str) -> bool:
            return 1 <= len(tag_name) <= 9 and all('A' <= c <= 'Z' for c in tag_name)

        # This flag tracks if at least one valid outer tag has been opened.
        # It helps enforce Rule 1: "The code must be wrapped in a valid closed tag."
        # If no tag is ever opened, or if a second root-level tag starts, it's invalid.
        found_first_tag = False

        while i < n:
            # Rule 7, 8: Prioritize CDATA parsing
            if i + 9 <= n and code[i:i+9] == "<![CDATA[":
                # Rule 4: CDATA must be inside a tag. If tag_stack is empty, it's not.
                if not tag_stack:
                    return False
                
                cdata_end_idx = code.find("]]>", i + 9) # Rule 7: find the first subsequent "]]>"
                if cdata_end_idx == -1:
                    return False # Rule 6: unmatched '<' if closing '>' (or ']]>') is not found
                
                i = cdata_end_idx + 3 # Move past "]]>"
                continue

            # Rule 2, 5: Check for End Tag (</TAG_NAME>)
            if i + 2 <= n and code[i:i+2] == "</":
                tag_end_idx = code.find(">", i + 2) # Rule 6: find subsequent '>'
                if tag_end_idx == -1:
                    return False # Unmatched '<'
                
                tag_name = code[i+2:tag_end_idx]
                
                # Rule 3: Validate TAG_NAME format. Rule 4: invalid TAG_NAME makes content invalid.
                if not is_valid_tag_name(tag_name):
                    return False
                
                # Rule 5: Unmatched/unbalanced tag
                if not tag_stack or tag_stack[-1] != tag_name:
                    return False
                
                tag_stack.pop()
                i = tag_end_idx + 1
                
                # Rule 1: If the tag_stack becomes empty AND we haven't reached the end of the string,
                # it means there are characters (plain text or another tag) after the outermost tag has closed.
                # This violates the single wrapper tag rule.
                if not tag_stack and i != n:
                    return False
                
                continue

            # Rule 2, 5: Check for Start Tag (<TAG_NAME>)
            if code[i] == '<': # If not CDATA and not an end tag, it must be a start tag
                tag_end_idx = code.find(">", i + 1) # Rule 6: find subsequent '>'
                if tag_end_idx == -1:
                    return False # Unmatched '<'
                
                tag_name = code[i+1:tag_end_idx]
                
                # Rule 3: Validate TAG_NAME format. Rule 4: invalid TAG_NAME makes content invalid.
                if not is_valid_tag_name(tag_name):
                    return False

                # Rule 1: If tag_stack is empty AND found_first_tag is True,
                # this indicates an attempt to open a second root-level tag after the first one closed. Invalid.
                # The first tag allows tag_stack to be empty and found_first_tag to be False.
                if not tag_stack and found_first_tag: 
                    return False
                
                tag_stack.append(tag_name)
                found_first_tag = True # Mark that we've successfully opened at least one tag
                i = tag_end_idx + 1
                continue
            
            # If current character is not '<' (i.e., it's plain text)
            # Rule 4: Plain text must be inside an opened tag.
            if not tag_stack:
                return False
            
            i += 1 # Move to the next character

        # After parsing the entire string:
        # 1. tag_stack must be empty to ensure all tags are properly closed (Rule 5).
        # 2. found_first_tag must be True to ensure the code wasn't empty or consisted only of plain text (Rule 1).
        return not tag_stack and found_first_tag

