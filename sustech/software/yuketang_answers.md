Here are the answers to the quizzes you provided:

---

## Quiz: Overview

### Q1 [1.单选题 (1分)]

Which principle suggests that catching a bug earlier in the development process is the most cost-effective?

- C. Shift Left

### Q2 [2.判断题 (1分)]

Software engineering is defined solely as the act of writing code.

- 错误 (False)

### Q3 [3.单选题 (1分)]

According to Hyrum's Law, what is a common challenge when an API has many consumers?

- B. Consumers may depende on undocumented behaviors, making changes difficult.

### Q4 [4.单选题 (1分)]

According to Frederick Brooks, what happens when you add manpower to a late software project?

- C. It makes the project even later.

---

## Quiz: Software Process

### Q1 [1.单选题 (1分)]

Which software process is not iterative?

- A. Waterfall

### Q2 [2.单选题 (1分)]

Which is not a Scrum artifact?

- B. Sprint review (Sprint review is a meeting/event, not an artifact)

### Q3 [3.单选题 (1分)]

What is a unique and central activity within each cycle of the Spiral model?

- D. Risk analysis and the evaluation of alternatives.

### Q4 [4.单选题 (1分)]

Under which circumstances is the Prototyping model most suitable to use?

- C. When the customer has a general idea for the software but has not defined detailed requirements.

### Q5 [5.单选题 (1分)]

What is a primary advantage of using an Incremental process model for software development?

- D. It allows for more rapid delivery and deployment of a usable core product.

---

## Quiz: Software Requirements

### Q1 [1.单选题 (1分)]

How are tasks related to user stories in Scrum?

- A. Tasks are used to break down user stories into smaller, actionable units of work.

### Q2 [2.单选题 (1分)]

In the Scrum process, who is primarily responsible for communicating with all stakeholders to gather requirements?

- B. The Product Owner

### Q3 [3.判断题 (1分)]

In a software project, primary stakeholders are the end-users, while secondary stakeholders are the developers and project managers.

- 错误 (False)

### Q4 [4.判断题 (1分)]

The primary purpose of software requirements is to describe what the system should do, the services it provides, and the constraints on its operation.

- 正确 (True)

---

## Quiz: VCS and git

### Q1 [1.单选题 (1分)]

Why are most operations in Git, such as viewing history or comparing versions, exceptionally fast?

- D. Most operations only need local files and resourses from the local database.

### Q2 [2.单选题 (1分)]

A developer runs `git pull` from their local repository. What two actions does this single command typically perform?

- B. It fetches data from the remote repository and then merge it into the current branch.

### Q3 [3.判断题 (1分)]

Git ensures data integrity by performing a checksum (SHA-1 hash) on every object before storing it.

- 正确 (True)

### Q4 [4.单选题 (1分)]

In the standard Git workflow, what is the role of the `git add` command?

- C. It transfers changes from the working directory to the staging area.

### Q5 [5.单选题 (1分)]

What is the fundamental difference in how Git stores data compared to centralized version control systems like SVN?

- D. Git stores a stream of snapshots of the entire project for each commit.

---

## Quiz: Software Architecture

### Q1 [1.判断题 (1分)]

Developers have to use the microservice architecture because it is better than the monolithic architecture.

- 错误 (False)

### Q2 [2.判断题 (1分)]

In layered architecture, the outermost layer is typically responsible for interacting with end users.

- 正确 (True)

### Q3 [3.判断题 (1分)]

Data-flow architecture is suitable for GUI intensive systems.

- 错误 (False)

### Q4 [4.单选题 (1分)]

In the context of microservice communication, what does it mean for a client to make a synchronous call?

- B. The client expects a timely response from the service and may block while waiting.

### Q5 [5.单选题 (1分)]

Which of the following is a defining characteristic of an event-driven architecture?

- C. Components communicate asynchronously by producing and consuming events.

### Q6 [6.单选题 (1分)]

In a data-centered architecture, what is the primary role of the central component?

- A. To serve as a repository that other components access to modify or retrieve data.

---

## Quiz: Software Build

### Q1 [1.单选题 (1分)]

When using the Bazel build system, if you change a single source file in a library that is a dependency for many other targets, what happens during the next build?

- B. Bazel rebuilds only the changed library and all the targets that transitively depend on it.

### Q2 [2.单选题 (1分)]

A project declares a dependency on a library with the version requirement "greater than or equal to 2.4.0". According to SemVer rules, which available library version would be unsafe to automatically update to?

- A. 3.0.0 (A major version increment indicates breaking changes, making it unsafe for automatic updates without review).

### Q3 [3.单选题 (1分)]

How does an artifact-based build system like Bazel achieve high performance through parallelism?

- B. By analyzing the declarative dependency graph to identify independent targets that can be built simultaneously.

### Q4 [4.单选题 (1分)]

What is a primary disadvantage of task-based build systems that artifact-based systems are designed to solve?

- D. They struggle with incremental builds and parallelism due to the arbitrary nature of tasks.

### Q5 [5.单选题 (1分)]

Which of the following best describes the core principle of a task-based build system like Maven or Ant?

- A. It defines the build process as a series of scripted tasks, where each task can have dependencies on other tasks.

### Q6 [6.单选题 (1分)]

What is the fundamental purpose of a build system in software engineering?

- C. To transform source code and all its related components into a complete, executable software.

---

## Quiz: Software Quality

### Q1 [1.单选题 (1分)]

What is the key insight from the Weighted Methods per Class (WMC) metric?

- D. It represents the overall complexity of a class by summing the complexities of its methods.

### Q2 [2.单选题 (1分)]

What is a potential downside of a class having a high DIT (Depth of Inheritance Tree) value?

- C. It can be harder to predict the class's behavior due to the large number of inherited methods.

### Q3 [3.单选题 (1分)]

What is the primary function of a linter?

- C. To analyze source code statically for stylistic issues, potential errors, and adhere to coding standards.

### Q4 [4.单选题 (1分)]

What does a high value for the Lack of Cohesion in Methods (LCOM) metric imply about a class's design?

- D. The class might be doing too many unrelated things and should potentially be split.

### Q5 [5.判断题 (1分)]

The primary purpose of the Cyclomatic Complexity metric is to quantify the logical complexity of a program based on its decision points.

- 正确 (True)

---

## Quiz: Software Testing

### Q1 [1.单选题 (1分)]

Which type of test double is best described as an object that provides predefined, hardcoded responses to method calls to get the system into a specific state?

- C. Stub

### Q2 [2.单选题 (1分)]

Why would a developer use a test double when testing a function that sends a request to an external server and stores the response in a database?

- C. To make the test suite run faster and be more reliable by avoiding network and database dependencies.

### Q3 [3.单选题 (1分)]

In blackbox testing, test cases are usually derived from:

- D. Use cases and functional requirements

### Q4 [4.单选题 (1分)]

If an if statement has a compound condition (e.g., if (A && B)), what does condition coverage aim to test?

- D. Whether each condition (A and B) evaluates to both true and false independently

### Q5 [5.判断题 (1分)]

Testers should be well aware of the internal implementations of SUT when performing black-box testing.

- 错误 (False)

### Q6 [6.单选题 (1分)]

The "Testing Pyramid" concept suggests a strategy for allocating testing effort. According to this model, which type of test should be the most numerous?

- C. Unit tests

### Q7 [7.单选题 (1分)]

According to the "Test Size" classification, what is a defining characteristic of a "small test"?

- D. It runs within a single process and avoids blocking calls like network requests.

### Q8 [8.判断题 (1分)]

A test suite is a collection or logical grouping of multiple test cases.

- 正确 (True)

---

## Quiz: CI/CD

### Q1 [1.判断题 (1分)]

Blue-Green Deployment can cause data consistency issues if stateful data is modified between versions.

- 正确 (True)

### Q2 [2.单选题 (1分)]

Before pushing changes to the central repository, what is a crucial local step a developer must perform after integrating the latest updates from their teammates?

- A. Rebuild the application and run tests to ensure the combined code works correctly.

### Q3 [3.单选题 (1分)]

Which software environment is described as a replica of the live environment, used for final validation and integration testing before updates are released to users?

- B. Staging environment

### Q4 [4.判断题 (1分)]

Continuous Deployment automatically releases every passed change to production, whereas Continuous Delivery requires a manual step for the final release.

- 正确 (True)

### Q5 [5.单选题 (1分)]

What is the fundamental goal of implementing Continuous Integration (CI) in a software development process?

- C. To automatically catch and identify problematic code changes as early as possible.

---

## Quiz: Cloud-native

### Q1 [1.单选题 (1分)]

What is the purpose of a Kubernetes Pod?

- D. The smallest deployable unit for running containers.

### Q2 [2.单选题 (1分)]

Why are containers considered more lightweight and resource-efficient than virtual machines?

- B. Containers package the application and its dependencies but share the host OS kernel.

### Q3 [3.判断题 (1分)]

A Docker image is a read-only template with instructions, and a container is a runnable instance of that image.

- 正确 (True)

### Q4 [4.单选题 (1分)]

Which is a significant drawback of deploying a service using the "Virtual Machine" pattern?

- A. Inefficient resource utilization due to the overhead of running a full OS for each service instance.

### Q5 [5.判断题 (1分)]

Scaling up involves adding more servers, while scaling out involves increasing the resources of a single server.

- 错误 (False - it's the other way around: scaling up means increasing resources of a single server; scaling out means adding more servers).

---

## Quiz: Maintenance and Evolution

### Q1 [1.单选题 (1分)]

What is the purpose of a "Sunset period" in the deprecation process?

- B. To provide consumers time to migrate before the system stops working.

### Q2 [2.单选题 (1分)]

Which pattern is recommended for incrementally refactoring a monolithic application into microservices?

- D. Strangler pattern

### Q3 [3.判断题 (1分)]

A "Code Smell" is a technical bug that prevents a program from functioning correctly.

- 错误 (False)

### Q4 [4.单选题 (1分)]

Which of the following is a key characteristic of "Refactoring"?

- C. It improves the internal structure while preserving external behavior.

### Q5 [5.判断题 (1分)]

Technical debt refers to the long-term cost of making suboptimal decisions in software design to meet short-term goals.

- 正确 (True)