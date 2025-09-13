import pytest
import asyncio
from unittest.mock import AsyncMock, patch
from agent.task_router import route_task

@pytest.mark.asyncio
async def test_route_task_success():
    # Arrange
    task = {"type": "summarize", "input": "This is a test."}
    mock_output = {"summary": "Short version."}

    with patch("models.summarize_model.run", new_callable=AsyncMock) as mock_run:
        mock_run.return_value = mock_output

        # Act
        result = await route_task(task)

        # Assert
        assert result == mock_output
        mock_run.assert_awaited_once_with("This is a test.")

@pytest.mark.asyncio
async def test_route_task_invalid_type():
    task = {"type": "unknown_model", "input": "Some input"}
    result = await route_task(task)
    assert "error" in result
    assert "Unsupported task type" in result["error"]
