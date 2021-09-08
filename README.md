# Example Conan project

This small project shows how one can create and consume Conan packages as dependencies, and how Conan integrates with Artifactory to create an easily used environment for handling these dependencies.

## Artifactory

Start an Artifactory instance, where we'll put our conan packages.

    docker run --name conan-artifactory -d -p 49001:8081 -p 49002:8082 docker.bintray.io/jfrog/artifactory-cpp-ce:latest

Create a new Conan repository.

Add the repository in the Artifactory instance as a remote in Conan.

    conan remote add <some_name> <url>

The url is on the form `http://<your_domain_and_possibly_port>/artifactory/api/conan/<name_of_repository>`, e.g. `https://localhost:49001/artifactory/api/conan/conan-packages.

On first time interacting with the remote, you'll be prompted for credentials.

More on the Conan [`user`](https://docs.conan.io/en/latest/reference/commands/misc/user.html).

## Conan

### Build the dependencies

We're starting from nothing so we'll have to first build and package the dependencies we're going to be using. These are the `givestring` and `sayhi` folders.

To create a Conan package, we run:

    conan create . <package_name>/<version>@<user>/channel

So, building `givestring` could, e.g., be done with:

    conan create . givestring/1.0@me/dev

And for `sayhi`, we'd have:

    conan create . sayhi/1.0@me/dev

### Upload dependencies to Artifactory

The dependencies we built are currently only available in our local conan cache. You can view it by running:

    conan search

To put the recipe(s) in our Artifactory repository, we can run:

    conan upload <package_name>/<version>@<user>/<channel> -r <the_remote>

We can add in the argument `--all` in order to upload both recipe and package, giving:

    conan upload givestring/1.0@me/dev --all -r conan-artifactory
    conan upload sayhi/1.0@me/dev --all -r conan-artifactory

### Build the main application

To build (and package) the main application, `project`, we can simply run the following:

    conan create . me/dev

and it will compile and run the test stuff under test_package.

If you prefer build it yourself, you can do some variation of:

    mkdir build && cd build
    conan install ..
    cmake .. && cmake --build . --config=Release

We can also delete our local cache (`~/.conan/data`), and rerun this last bit, to see that it really fetches the packages from Artifactory.

