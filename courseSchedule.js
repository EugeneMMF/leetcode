/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
  let i=0;
  let courses = new Set(Array.from(Array(numCourses), () => (i++).toString()));
  i = 0;
  let order = Object.fromEntries(Array.from(Array(numCourses), () => [(i++).toString(), new Set()]));
  for (let [second,first] of prerequisites) {
    order[second.toString()].add(first.toString());
  }
  let toLookAt = new Set(Array.from(courses.values()));
  while (toLookAt.size) {
    let value = toLookAt.values().next().value;
    toLookAt.delete(value);
    if (order[value].size == 0) {
      courses.delete(value);
      for (key of Object.keys(order)) {
        if (order[key].delete(value)) {
          toLookAt.add(key);
        }
      }
    }
  }
  return courses.size == 0;
};