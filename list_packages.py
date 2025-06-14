import pkg_resources
import site

# Get all installed packages
for dist in pkg_resources.working_set:
    print(f"Package: {dist.key}, Version: {dist.version}, Location: {dist.location}")