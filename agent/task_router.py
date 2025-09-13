# agent/task_router.py

import importlib
from registry.registry_loader import load_registry

# Load the model registry (cached after first read)
model_registry = load_registry()

async def route_task(task: dict):
    """
    Route the incoming task to the correct model's run() method.
    """
    task_type = task.get("type")
    input_data = task.get("input", "")

    # Validate task type
    if task_type not in model_registry:
        return {"error": f"Unsupported task type: {task_type}"}

    model_config = model_registry[task_type]

    # Dynamic module + function load
    try:
        module_path = model_config["module"]
        function_name = model_config["function"]

        module = importlib.import_module(module_path)
        model_func = getattr(module, function_name)

        # Run model (assumed async)
        result = await model_func(input_data)
        return result

    except Exception as e:
        return {"error": f"Failed to run model: {str(e)}"}
