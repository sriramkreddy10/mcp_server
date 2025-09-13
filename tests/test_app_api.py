import pytest
from httpx import AsyncClient, ASGITransport
from unittest.mock import patch, AsyncMock
from app import app  # make sure this is imported correctly

@pytest.mark.asyncio
async def test_api_chat_success():
    mock_response = {"reply": "Sure, happy to help!"}
    test_input = {"type": "chat", "input": "Hello, how are you?"}

    with patch("models.chat_model.run", new_callable=AsyncMock) as mock_run:
        mock_run.return_value = mock_response

        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.post("/task", json=test_input)
            assert response.status_code == 200
            assert response.json() == mock_response
