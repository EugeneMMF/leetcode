class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        pos_set = set(positive_feedback)
        neg_set = set(negative_feedback)
        points = {}
        for rid, txt in zip(student_id, report):
            pts = 0
            for w in txt.split():
                if w in pos_set:
                    pts += 3
                elif w in neg_set:
                    pts -= 1
            points[rid] = pts
        sorted_ids = sorted(points.keys(), key=lambda x: (-points[x], x))
        return sorted_ids[:k]