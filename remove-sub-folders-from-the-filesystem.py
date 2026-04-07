class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()

        result = []

        for current_folder in folder:
            if not result:
                result.append(current_folder)
            else:
                last_root_folder = result[-1]
                if not current_folder.startswith(last_root_folder + "/"):
                    result.append(current_folder)
        
        return result