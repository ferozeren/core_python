# %% [markdown]
# # Variables in Python: Usage, Mechanics & Scopes
# Clean, runnable examples breaking down reference semantics, naming patterns,
# memory behavior, unpacking, pattern matching, and scope rules.

# %%
# Variables as Named References
print("\n--- Variables as Named References ---")

# In Python, variables do not store values directly; they point to objects in memory.
val_a: int = 300
val_b: int = val_a

print(f"val_a: {val_a}, id: {id(val_a)}")
print(f"val_b: {val_b}, id: {id(val_b)}")
print(f"Points to identical object: {val_a is val_b}")

# Reassigning val_b creates a new reference; val_a remains untouched.
val_b = 400
print(f"After reassignment -> val_a: {val_a}, val_b: {val_b}")
print(f"val_b new id: {id(val_b)}")

# %%
# Dynamic Typing & Type Mutation Hazards
print("\n--- Dynamic Typing & Hazards ---")

# Variables can bind to any data type over time without declaration changes.
dynamic_item: int | str = 42
print(f"Initial: {dynamic_item} (type: {type(dynamic_item).__name__})")

dynamic_item = "running_process"
print(f"Reassigned: {dynamic_item} (type: {type(dynamic_item).__name__})")

# Runtime check: methods must belong to the active type
if isinstance(dynamic_item, str):
    print("Upper string:", dynamic_item.upper())
else:
    print("Not a string, skipping .upper()")

# %%
# Idiomatic Usage: Counters, Accumulators & Flags
print("\n--- Counters, Accumulators & Flags ---")

# Object counter
raw_records: tuple[object, ...] = ("sensor_1", 23.4, None, "sensor_2", 45, True)
string_count: int = 0

for record in raw_records:
    if isinstance(record, str):
        string_count += 1
print(f"Found {string_count} string items")

# Accumulator
metrics: list[float] = [10.5, 20.0, 32.5, 5.0]
running_total: float = 0.0

for reading in metrics:
    running_total += reading
mean_metric: float = running_total / len(metrics) if metrics else 0.0
print(f"Total: {running_total}, Mean: {mean_metric}")

# State flags
is_connected: bool = True
has_pending_jobs: bool = False
should_retry: bool = not is_connected or has_pending_jobs
print(f"Should retry operation: {should_retry}")

# %%
# 4. Multi-Assignment & Iterable Unpacking
print("\n--- Unpacking & Swapping ---")

# Parallel broadcast
default_timeout = retry_limit = max_workers = 5
print(f"Broadcast configs: {default_timeout}, {retry_limit}, {max_workers}")

# In-place swapping (no temp variable needed)
reg_x: int = 10
reg_y: int = 99
reg_x, reg_y = reg_y, reg_x
print(f"Swapped: reg_x={reg_x}, reg_y={reg_y}")

# Sequence unpacking with throwaways and remainder captures
payload: tuple[str, str, int, str, str] = (
    "2026-11-08",
    "WARN",
    503,
    "192.168.1.1",
    "gateway_timeout",
)
timestamp, level, status_code, *network_info = payload

print(f"Parsed header: [{level}] at {timestamp} -> status {status_code}")
print(f"Remaining payload fields: {network_info}")

# Ignoring values explicitly with '_'
user_row: tuple[str, str, str] = ("Feroze", "dev@local", "Hyderabad")
username, _, city = user_row
print(f"User: {username}, City: {city}")

# %%
# Modern Assignment: Walrus (:=) & Pattern Matching
print("\n--- Assignment Expressions & Pattern Matching ---")

# Walrus operator := assigns and evaluates simultaneously inside a condition
buffer: list[int] = [4, 8, 15, 16, 23, 42]
if (n_items := len(buffer)) > 3:
    print(f"Buffer queue is high: {n_items} items queued")

# Structural Pattern Matching (captures variables in-scope on match)


def matchable_action(action: tuple[str, int, int] | tuple[str, int]) -> None:
    match action:
        case ("click", x, y):
            print(f"Action: Click at ({x}, {y})")
        case ("move_cursor", x, y):
            print(f"Action: Move pointer to ({x}, {y})")
        case ("key_press", key_code):
            print(f"Action: Key down {key_code}")
        case _:
            print("Unknown command format")


action: tuple[str, int, int] | tuple[str, int] = ("move_cursor", 120, 450)

matchable_action(action)
matchable_action(("key_press", 1))


# %%
# Container Type Annotations
print("\n--- Explicit Collection Typing ---")

# Primitive type hints are often clear from literal values,
# but container structures benefit heavily from inner type clarity.
user_scores: dict[str, int] = {"alpha": 12, "beta": 45}
empty_queue: list[tuple[int, str]] = []

empty_queue.append((1, "job_init"))
empty_queue.append((2, "job_process"))

print(f"Queue entries: {empty_queue}")
print(f"Scores map: {user_scores}")

# %%
# Variable Scope: The LEGB Rule (Local, Enclosing, Global, Built-in)
print("\n--- Variable Scopes ---")

system_env: str = "PRODUCTION"  # Global scope


def outer_service() -> None:
    session_id: str = "sess_9021"  # Enclosing scope

    def inner_worker() -> None:
        task_id: str = "task_01"  # Local scope
        print(f"Inner worker sees Local: {task_id}")
        print(f"Inner worker sees Enclosing: {session_id}")
        print(f"Inner worker sees Global: {system_env}")

    inner_worker()


outer_service()

# Mutating outer scopes requires explicit keywords
counter: int = 0


def update_counters() -> None:
    global counter
    counter += 1

    offset: int = 10

    def nested_shift() -> None:
        nonlocal offset
        offset += 5

    nested_shift()
    print(f"Enclosing offset modified to: {offset}")


update_counters()
print(f"Global counter modified to: {counter}")

# %%
# Class Attributes vs Instance Attributes
print("\n--- Class Attributes vs Instance Attributes ---")


class WorkerNode:
    # Class attribute: shared state across every instance
    node_pool_count: int = 0

    def __init__(self, node_id: str, capacity: int) -> None:
        # Instance attributes: strictly unique to this object
        self.node_id: str = node_id
        self.capacity: int = capacity
        WorkerNode.node_pool_count += 1

    def state(self) -> str:
        return f"Node {self.node_id} [cap: {self.capacity}]"


node_1 = WorkerNode("sg-01", 64)
node_2 = WorkerNode("sg-02", 128)


print(node_1.state())
print(node_2.state())
print(f"Shared WorkerNode count via class: {WorkerNode.node_pool_count}")
print(f"Shared WorkerNode count via instance: {node_1.node_pool_count}")

# Mutation distinction:
# Modifying on the instance creates an instance attribute shadow, not a class update.
node_1.node_pool_count = 999
print(f"Shadowed attribute on node_1: {node_1.node_pool_count}")
print(f"Actual class attribute stays: {WorkerNode.node_pool_count}")

# %%
# Namespace Cleanup: del Statement
print("\n--- Explicit Deletion (del) ---")

cached_token: str | None = "temp_auth_token_xyz"
print(f"Token active: {cached_token}")

# del unbinds the name from current scope; reference count drops
del cached_token

try:
    # pyrefly: ignore[unbound-name]
    print(cached_token)
except NameError as err:
    print(f"Accessing unbound variable raised expected error: {err}")
