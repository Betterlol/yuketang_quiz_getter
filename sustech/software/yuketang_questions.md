# 雨课堂 题库汇总

- 课程链接: https://sustc.yuketang.cn/pro/lms/8MuSR5nESwE/29477711/studycontent
- 导出时间: 2026-05-31 18:27:21
- Quiz 总数: 11
- 题目总数: 58

---

## Quiz: Overview

### Q1 [1.单选题 (1分)]

Which principle suggests that catching a bug earlier in the development process is the most cost-effective?

- A. Scale
- B. No Silver Bullet
- C. Shift Left
- D. Hyrum's Law

---

### Q2 [2.判断题 (1分)]

Software engineering is defined solely as the act of writing code.

---

### Q3 [3.单选题 (1分)]

According to Hyrum's Law, what is a common challenge when an API has many consumers?

- A. The API becomes faster to evolve.
- B. Consumers may depende on undocumented behaviors, making changes difficult.
- C. Consumers only depend on documented features.
- D. It becomes easier to maintain backward compatibility.

---

### Q4 [4.单选题 (1分)]

According to Frederick Brooks, what happens when you add manpower to a late software project?

- A. It finishes on time.
- B. It finishes faster but with more bugs.
- C. It makes the project even later.
- D. The quality of the software improves significantly.

---

## Quiz: Software Process

### Q1 [1.单选题 (1分)]

Which software process is not iterative?

- A. Waterfall
- B. Prototyping
- C. Spiral
- D. Scrum

---

### Q2 [2.单选题 (1分)]

Which is not a Scrum artifact?

- A. Burndown charts
- B. Sprint review
- C. Sprint backlog
- D. Product backlog

---

### Q3 [3.单选题 (1分)]

What is a unique and central activity within each cycle of the Spiral model?

- A. Conducting a daily stand-up meeting to synchronize team efforts.
- B. Delivering a small, usable increment of the final product.
- C. Signing off on comprehensive documentation before any coding begins.
- D. Risk analysis and the evaluation of alternatives.

---

### Q4 [4.单选题 (1分)]

Under which circumstances is the Prototyping model most suitable to use?

- A. When the team needs to deliver a series of increasingly complete, shippable software releases.
- B. When the customer can provide a detailed and stable list of all features and functions at the start.
- C. When the customer has a general idea for the software but has not defined detailed requirements.
- D. When the project is high-risk and requires iterative risk assessment, such as for a medical system.

---

### Q5 [5.单选题 (1分)]

What is a primary advantage of using an Incremental process model for software development?

- A. It eliminates the need for initial planning and design, allowing the team to start coding immediately.
- B. It ensures that the overall system architecture remains pristine and never degraded over time.
- C. It is the best model when all project requirements are stable and clearly defined from the very beginning.
- D. It allows for more rapid delivery and deployment of a usable core product.

---

## Quiz: Software Requirements

### Q1 [1.单选题 (1分)]

How are tasks related to user stories in Scrum?

- A. Tasks are used to break down user stories into smaller, actionable units of work.
- B. Tasks are written by the product owner while user stories are written by the developers.
- C. Tasks and user stories are interchangeable terms for the same requirements.
- D. Tasks are high-level requirements that are grouped into a single user story.

---

### Q2 [2.单选题 (1分)]

In the Scrum process, who is primarily responsible for communicating with all stakeholders to gather requirements?

- A. The Project Manager
- B. The Product Owner
- C. The Development Team
- D. The Scrum Master

---

### Q3 [3.判断题 (1分)]

In a software project, primary stakeholders are the end-users, while secondary stakeholders are the developers and project managers.

---

### Q4 [4.判断题 (1分)]

The primary purpose of software requirements is to describe what the system should do, the services it provides, and the constraints on its operation.

---

## Quiz: VCS and git

### Q1 [1.单选题 (1分)]

Why are most operations in Git, such as viewing history or comparing versions, exceptionally fast?

- A. They rely on high-speed network connections to a powerful central server.
- B. Git compresses its data more efficiently than any other version control system.
- C. Git limits the project history that can be browsed at any one time.
- D. Most operations only need local files and resourses from the local database.

---

### Q2 [2.单选题 (1分)]

A developer runs gitp l − from their local repository. What two actions does this single command typically perform?

- A. It checks the status of the local repository and then fetches data from the remote.
- B. It fetches data from the remote repository and then merge it into the current branch.
- C. It stages the current changes and then commit them to the local repository.
- D. It commits the current changes and then pushes them to the remote repository.

---

### Q3 [3.判断题 (1分)]

Git ensures data integrity by performing a checksum (SHA-1 hash) on every object before storing it.

---

### Q4 [4.单选题 (1分)]

In the standard Git workflow, what is the role of the gitadd command?

- A. It uploads the selected file changes from the local repository to the remote repository.
- B. It adds a new untracked file to the working directory for Git to be aware of.
- C. It transfers changes from the working directory to the staging area.
- D. It permanently saves the current changes to the local repository's history.

---

### Q5 [5.单选题 (1分)]

What is the fundamental difference in how Git stores data compared to centralized version control systems like SVN?

- A. Git stores the differences for each file, which is more space-efficient.
- B. Git only stores a single version of the files on a central server.
- C. Git stores changes as patch sets on disk that are applied sequentially to recreate a file.
- D. Git stores a stream of snapshots of the entire project for each commit.

---

## Quiz: Software Architecture

### Q1 [1.判断题 (1分)]

Developers have to use the microservice architecture because it is better than the monolithic architecture.

---

### Q2 [2.判断题 (1分)]

In layered architecture, the outermost layer is typically responsible for interacting with end users.

---

### Q3 [3.判断题 (1分)]

Data-flow architecture is suitable for GUI intensive systems.

---

### Q4 [4.单选题 (1分)]

In the context of microservice communication, what does it mean for a client to make a synchronous call?

- A. The client communicates by publishing an event to a shared message broker.
- B. The client expects a timely response from the service and may block while waiting.
- C. The client and service must be written in the same programming language.
- D. The client sends a message and immediately continues with its own processing.

---

### Q5 [5.单选题 (1分)]

Which of the following is a defining characteristic of an event-driven architecture?

- A. A central data store is the sole medium for communication between components.
- B. All application functionality is bundled into a single process.
- C. Components communicate asynchronously by producing and consuming events.
- D. A strict, hierarchical control structure where a main program calls subprograms.

---

### Q6 [6.单选题 (1分)]

In a data-centered architecture, what is the primary role of the central component?

- A. To serve as a repository that other components access to modify or retrieve data.
- B. To sequentially process data through a series of transformations.
- C. To manage the control hierarchy by invoking various subprograms.
- D. To handle user interface operations and display information to the user.

---

## Quiz: Software Build

### Q1 [1.单选题 (1分)]

When using the Bazel build system, if you change a single source file in a library that is a dependency for many other targets, what happens during the next build?

- A. Only the library containing the changed file will be rebuilt; its dependencies are reused from the cache.
- B. Bazel rebuilds only the changed library and all the targets that transitively depend on it.
- C. Bazel waits for the user to manually specify which targets need to be rebuilt.
- D. The entire project must be rebuilt from scratch to ensure consistency.

---

### Q2 [2.单选题 (1分)]

A project declares a dependency on a library with the version requirement "greater than or equal to 2.4.0". According to SemVer rules, which available library version would be unsafe to automatically update to?

- A. 3.0.0
- B. 2.4.7
- C. 2.4.0
- D. 2.5.0

---

### Q3 [3.单选题 (1分)]

How does an artifact-based build system like Bazel achieve high performance through parallelism?

- A. By requiring engineers to write multi-threaded scripts for each build task.
- B. By analyzing the declarative dependency graph to identify independent targets that can be built simultaneously.
- C. By executing all build phases at the same time regardless of their order.
- D. By caching the final executable and only distributing it to multiple cores for testing.

---

### Q4 [4.单选题 (1分)]

What is a primary disadvantage of task-based build systems that artifact-based systems are designed to solve?

- A. They require engineers to write buildfiles in a specific format like XML.
- B. They cannot manage dependencies on third-party libraries.
- C. They are incompatible with modern DevOps practice and continuous integration pipelines.
- D. They struggle with incremental builds and parallelism due to the arbitrary nature of tasks.

---

### Q5 [5.单选题 (1分)]

Which of the following best describes the core principle of a task-based build system like Maven or Ant?

- A. It defines the build process as a series of scripted tasks, where each task can have dependencies on other tasks.
- B. It automatically analyzes source code to create a dependency graph of artifacts before any execution.
- C. It requires engineers to declare a manifest of artifacts, and the system determines how to build them.
- D. It focuses exclusively on packaging compiled code into a distributable format like a JAR or EXE file.

---

### Q6 [6.单选题 (1分)]

What is the fundamental purpose of a build system in software engineering?

- A. To solely compile source code into machine code using a compiler like javac.
- B. To write shell scripts that automate the execution of the final program.
- C. To transform source code and all its related components into a complete, executable software.
- D. To manage different versions of source code in a repository like Git.

---

## Quiz: Software Quality

### Q1 [1.单选题 (1分)]

What is the key insight from the Weighted Methods per Class (WMC) metric?

- A. It measures how many other classes a given class interacts with.
- B. It counts the number of child classes that inherit from a parent class.
- C. It determines if methods in a class operate on shared fields.
- D. It represents the overall complexity of a class by summing the complexities of its methods.

---

### Q2 [2.单选题 (1分)]

What is a potential downside of a class having a high DIT (Depth of Inheritance Tree) value?

- A. It makes the class highly reusable in different contexts.
- B. It indicates the class has no relationship to any other class in the system.
- C. It can be harder to predict the class's behavior due to the large number of inherited methods.
- D. It means the class methods are not cohesive and should be split into smaller classes.

---

### Q3 [3.单选题 (1分)]

What is the primary function of a linter?

- A. To execute the code and identify runtime errors or bugs.
- B. To convert source code from a high-level language to machine code.
- C. To analyze source code statically for stylistic issues, potential errors, and adhere to coding standards.
- D. To automatically generate documentation based on code comments.

---

### Q4 [4.单选题 (1分)]

What does a high value for the Lack of Cohesion in Methods (LCOM) metric imply about a class's design?

- A. The class is heavily relied upon by many other classes throughout the system.
- B. The methods within the class are highly related and work together on shared data.
- C. The class is very abstract and sits at the top of an inheritance hierarchy.
- D. The class might be doing too many unrelated things and should potentially be split.

---

### Q5 [5.判断题 (1分)]

The primary purpose of the Cyclomatic Complexity metric is to quantify the logical complexity of a program based on its decision points.

---

## Quiz: Software Testing

### Q1 [1.单选题 (1分)]

Which type of test double is best described as an object that provides predefined, hardcoded responses to method calls to get the system into a specific state?

- A. Mock
- B. Fake
- C. Stub
- D. Proxy

---

### Q2 [2.单选题 (1分)]

Why would a developer use a test double when testing a function that sends a request to an external server and stores the response in a database?

- A. To replace the system under test with a stand-in object.
- B. To verify that the external server and database are online and responding correctly.
- C. To make the test suite run faster and be more reliable by avoiding network and database dependencies.
- D. To ensure 100% code coverage of the external server's API.

---

### Q3 [3.单选题 (1分)]

In blackbox testing, test cases are usually derived from:

- A. Control flow graphs
- B. Code coverage analysis
- C. Static analysis
- D. Use cases and functional requirements

---

### Q4 [4.单选题 (1分)]

If an if statement has a compound condition (e.g., if (A && B)), what does condition coverage aim to test?

- A. Only true outcomes of the condition
- B. Whether both A and B are true together
- C. Every possible combination of A and B
- Whether each condition (A and B) evaluates to both true and false independently

---

### Q5 [5.判断题 (1分)]

Testers should be well aware of the internal implementations of SUT when performing black-box testing.

---

### Q6 [6.单选题 (1分)]

The "Testing Pyramid" concept suggests a strategy for allocating testing effort. According to this model, which type of test should be the most numerous?

- A. E2E tests
- B. Integration tests
- C. Unit tests
- D. Manual tests

---

### Q7 [7.单选题 (1分)]

According to the "Test Size" classification, what is a defining characteristic of a "small test"?

- A. It can make network calls, but only to services on the localhost.
- B. It runs across multiple machines to validate network configuration.
- C. It requires manual intervention from a tester to execute.
- D. It runs within a single process and avoids blocking calls like network requests.

---

### Q8 [8.判断题 (1分)]

A test suite is a collection or logical grouping of multiple test cases.

---

## Quiz: CI/CD

### Q1 [1.判断题 (1分)]

Blue-Green Deployment can cause data consistency issues if stateful data is modified between versions.

---

### Q2 [2.单选题 (1分)]

Before pushing changes to the central repository, what is a crucial local step a developer must perform after integrating the latest updates from their teammates?

- A. Rebuild the application and run tests to ensure the combined code works correctly.
- B. Immediately push the merged code to let the CI server find any conflicts.
- C. Wait for the CI server to become available before pulling any new changes.
- D. Document the changes in a separate file before pushing.

---

### Q3 [3.单选题 (1分)]

Which software environment is described as a replica of the live environment, used for final validation and integration testing before updates are released to users?

- A. Production environment
- B. Staging environment
- C. Local environment
- D. Development environment

---

### Q4 [4.判断题 (1分)]

Continuous Deployment automatically releases every passed change to production, whereas Continuous Delivery requires a manual step for the final release.

---

### Q5 [5.单选题 (1分)]

What is the fundamental goal of implementing Continuous Integration (CI) in a software development process?

- A. To replace the need for developers to write unit tests for their code.
- B. To enforce a monthly release cycle for all software projects.
- C. To automatically catch and identify problematic code changes as early as possible.
- D. To automate the final deployment of software directly to end-users without any testing.

---

## Quiz: Cloud-native

### Q1 [1.单选题 (1分)]

What is the purpose of a Kubernetes Pod?

- A. A control plane for scheduling workloads.
- B. A proxy for load balancing.
- C. A monitoring tool.
- D. The smallest deployable unit for running containers.

---

### Q2 [2.单选题 (1分)]

Why are containers considered more lightweight and resource-efficient than virtual machines?

- A. Containers require significantly more RAM and CPU to boot up than VMs.
- B. Containers package the application and its dependencies but share the host OS kernel.
- C. Containers include a full copy of the host operating system.
- D. Containers run on a dedicated physical machine for each instance.

---

### Q3 [3.判断题 (1分)]

A Docker image is a read-only template with instructions, and a container is a runnable instance of that image.

---

### Q4 [4.单选题 (1分)]

Which is a significant drawback of deploying a service using the "Virtual Machine" pattern?

- A. Inefficient resource utilization due to the overhead of running a full OS for each service instance.
- B. It is impossible to constrain the CPU or memory resources consumed by a service instance.
- C. The operations team must know the specific language and runtime version for each service.
- D. Lack of isolation between different service instances running on the same hardware.

---

### Q5 [5.判断题 (1分)]

Scaling up involves adding more servers, while scaling out involves increasing the resources of a single server.

---

## Quiz: Maintenance and Evolution

### Q1 [1.单选题 (1分)]

What is the purpose of a "Sunset period" in the deprecation process?

- A. To allow developers to delete all old code immediately.
- B. To provide consumers time to migrate before the system stops working.
- C. To fix all bugs in the deprecated system.
- D. To hide the deprecated API from new users.

---

### Q2 [2.单选题 (1分)]

Which pattern is recommended for incrementally refactoring a monolithic application into microservices?

- A. Big Bang pattern
- B. Shotgun pattern
- C. Legacy-first pattern
- D. Strangler pattern

---

### Q3 [3.判断题 (1分)]

A "Code Smell" is a technical bug that prevents a program from functioning correctly.

---

### Q4 [4.单选题 (1分)]

Which of the following is a key characteristic of "Refactoring"?

- A. It changes the external behavior to improve performance.
- B. It is used primarily to add new features to the system.
- C. It improves the internal structure while preserving external behavior.
- D. It involves rewriting the system from scratch to fix bugs.

---

### Q5 [5.判断题 (1分)]

Technical debt refers to the long-term cost of making suboptimal decisions in software design to meet short-term goals.

---

