class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        exclusive_times = [0] * n
        call_stack = []  # Stores function_id of currently executing functions
        # prev_timestamp tracks the timestamp of the last log event,
        # or the effective start time of the current top-of-stack function's segment.
        prev_timestamp = 0

        for log_entry in logs:
            parts = log_entry.split(':')
            function_id = int(parts[0])
            event_type = parts[1]
            timestamp = int(parts[2])

            if event_type == "start":
                if call_stack:
                    # A function was running, and now it's being interrupted.
                    # Calculate the time it ran from prev_timestamp up to (but not including)
                    # the current timestamp, and add it to its exclusive time.
                    currently_running_fid = call_stack[-1]
                    exclusive_times[currently_running_fid] += timestamp - prev_timestamp
                
                # Push the new function's ID onto the stack as it starts execution.
                call_stack.append(function_id)
                # Update prev_timestamp to the current timestamp. This timestamp
                # will be used to calculate the duration of the *next* segment.
                prev_timestamp = timestamp
            else:  # event_type == "end"
                # The function at the top of the stack must be the one ending.
                popped_fid = call_stack.pop()
                
                # Calculate the exclusive time for this specific call of the function.
                # It ran from prev_timestamp up to (and including) the current timestamp.
                exclusive_times[popped_fid] += timestamp - prev_timestamp + 1
                
                # Update prev_timestamp to the timestamp *after* this function ended.
                # If a parent function resumes, its new segment of execution effectively
                # starts right after this one finished.
                prev_timestamp = timestamp + 1
        
        return exclusive_times
