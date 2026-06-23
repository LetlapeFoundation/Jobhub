# Contributing to JobHub

Thank you for considering contributing to JobHub! This document provides guidelines and instructions for developers.

## Code of Conduct

- Be respectful and inclusive
- Follow the Constitution v2.0 principles (accessibility, trust, sovereignty, fairness)
- Test your code before submitting
- Document your changes

## Development Workflow

### 1. Set Up Local Environment

```bash
git clone https://github.com/LetlapeFoundation/Jobhub.git
cd Jobhub
cp .env.example .env
docker-compose up -d

# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
python -m uvicorn app.main:app --reload

# Frontend (new terminal)
cd frontend
npm install
npm run dev
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/short-description
# or
git checkout -b fix/issue-number
```

### 3. Make Your Changes

- Follow PEP 8 (Python) and ESLint (JavaScript/TypeScript) standards
- Write tests for new features
- Update documentation if needed
- Keep commits small and focused

### 4. Run Tests & Linting

**Backend:**
```bash
cd backend
pytest                    # Run tests
black .                   # Format code
flake8 .                  # Lint
mypy .                    # Type check
```

**Frontend:**
```bash
cd frontend
npm run test              # Run tests
npm run lint              # Lint
npm run format            # Format
```

### 5. Commit & Push

```bash
git add .
git commit -m "feat: describe your change"
git push origin feature/short-description
```

Commit message format:
- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation
- `refactor:` code refactoring
- `test:` test additions/changes
- `chore:` tooling, config

### 6. Create a Pull Request

- Push your branch and create a PR against `main`
- Link any related issues (e.g., "Fixes #42")
- Describe what you changed and why
- Ensure CI passes (tests, lint, type checks)

## Coding Standards

### Python (Backend)

- Style: PEP 8 (enforced with Black)
- Type hints: Mandatory for all functions
- Docstrings: Google-style format
- Max line length: 88 characters

```python
def create_user(email: str, password: str) -> User:
    """Create a new user account.
    
    Args:
        email: User email address (must be unique)
        password: Plain-text password (will be hashed)
    
    Returns:
        User: The newly created user object
    
    Raises:
        ValueError: If email already exists
    """
    # Implementation
```

### TypeScript/React (Frontend)

- Style: ESLint + Prettier
- Type hints: Mandatory for all functions
- Functional components with hooks
- Props interfaces at top of file

```typescript
interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
}

function Button({ label, onClick, disabled = false }: ButtonProps) {
  return (
    <button onClick={onClick} disabled={disabled}>
      {label}
    </button>
  );
}
```

## Testing Requirements

### Backend Tests

Write pytest tests for:
- API endpoints (request/response)
- Business logic (services)
- Database models
- Security/auth functions

```python
# tests/api/test_jobs.py
def test_create_job_success(client, employer_verified):
    """Employer can create a job posting."""
    response = client.post(
        "/api/v1/jobs",
        json={
            "title": "Python Developer",
            "description": "Junior role",
            "salary_min": 25000,
            "salary_max": 35000,
        },
        headers={"Authorization": f"Bearer {employer_verified.token}"},
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Python Developer"
```

### Frontend Tests

Write Jest/Vitest tests for:
- Component rendering
- User interactions
- API integration (mocked)
- State management

```typescript
// src/components/__tests__/JobCard.test.tsx
it('should render job title and salary', () => {
  const job = { id: 1, title: 'Engineer', salary_min: 50000, salary_max: 70000 };
  const { getByText } = render(<JobCard job={job} />);
  expect(getByText('Engineer')).toBeInTheDocument();
  expect(getByText(/50000 - 70000/)).toBeInTheDocument();
});
```

## Documentation

Update documentation for:
- New API endpoints (`docs/API.md`)
- Architecture changes (`docs/ARCHITECTURE.md`)
- Deployment procedures (`docs/DEPLOYMENT.md`)
- Bug fixes or feature changes (update README if user-facing)

## Performance & Security Guidelines

### Backend
- Use database indexes for frequently queried columns
- Implement query pagination (max 100 items per request)
- Hash all passwords with bcrypt (min 12 rounds)
- Validate all user input with Pydantic schemas
- Log security events (failed logins, unauthorized access)
- Never log PII (passwords, IDs, banking details)

### Frontend
- Lazy-load routes and components
- Use React.memo for expensive components
- Minimize bundle size (split code by route)
- Never store secrets in localStorage
- Use HTTPS in production
- Sanitize all user input before rendering

## CRYTONET Integration

When working with identity verification or fraud detection:
- Use CRYTONET test keys in development (`.env.example` provided)
- Mock CRYTONET responses in tests (do not call production API)
- Log all CRYTONET events for audit trail
- Never bypass verification checks (even in dev)

## Database Migrations

When modifying database schema:

```bash
cd backend
alembic revision --autogenerate -m "describe the change"
alembic upgrade head  # Test locally
```

Always:
- Write both upgrade and downgrade scripts
- Test migrations on a copy of production data
- Never use ALTER TABLE without checking backward compatibility

## Reporting Issues

If you find a bug:
1. Check if it's already reported (search GitHub Issues)
2. Provide:
   - Clear title and description
   - Steps to reproduce
   - Expected vs. actual behavior
   - Environment (OS, browser, Python version, etc.)
   - Screenshots/logs if applicable

## Questions?

- Open a GitHub Discussion
- Check existing documentation (`docs/`)
- Reach out to the team

---

**Thank you for building JobHub! 🚀**
