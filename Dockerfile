# ---------- Stage 1: Builder ----------
FROM python:3.11-slim AS builder

WORKDIR /build

# Install dependencies separately for caching
COPY app/requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ---------- Stage 2: Runtime ----------
FROM python:3.11-slim

WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY app /app/app

# Create non-root user (best practice)
RUN useradd -m appuser
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]