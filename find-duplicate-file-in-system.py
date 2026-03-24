
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        content_to_paths = defaultdict(list)

        for path_info_string in paths:
            parts = path_info_string.split(' ')
            directory_path = parts[0]
            
            for file_info_string in parts[1:]:
                open_paren_idx = file_info_string.find('(')
                close_paren_idx = file_info_string.find(')')
                
                file_name = file_info_string[:open_paren_idx]
                file_content = file_info_string[open_paren_idx + 1:close_paren_idx]
                
                full_file_path = f"{directory_path}/{file_name}"
                content_to_paths[file_content].append(full_file_path)
        
        result = []
        for paths_list in content_to_paths.values():
            if len(paths_list) > 1:
                result.append(paths_list)
                
        return result
