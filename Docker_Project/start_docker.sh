docker build -t resumeproj .
docker run -p 8501:8501 -v "$(realpath ~/Downloads):/app/output" resumeproj
