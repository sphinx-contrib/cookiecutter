def test_project_tree(cookies):
    result = cookies.bake(
        extra_context={
            "github_org": "johndoe",
            "project_name": "project-name",
            "short_description": "Short description",
            "author_name": "John Doe",
            "author_email": "john@doe.me",
        }
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "project-name"
    assert result.project_path.is_dir()

    files = [
        ".gitignore",
        "LICENSE",
        "README.md",
        "pyproject.toml",
        "tox.ini",
    ]
    dirs = [
        "src",
        "src/project_name",
        "docs",
        "docs/source",
        "tests",
        "tests/cases",
    ]

    for path in files:
        assert (result.project_path / path).is_file()
    for path in dirs:
        assert (result.project_path / path).is_dir()
