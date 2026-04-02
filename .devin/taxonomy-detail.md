## Robotics Skills Framework Design Principles

(a) The separation of Methodology Tracks (T2–T5) from Application Tracks (T6–T7) allows learners to focus on areas aligned with their target roles; 
(b) L0–L4 are defined by dependency relationships rather than experience levels, ensuring the learning path is logically rigorous;
(c) T1 and T8 serve as foundational layers that run throughout the entire framework, reflecting the industry's demand for "full-stack robotics engineers." 
(d) The **eight Tracks** are organized into three tiers: Foundation (T1 & T8), Methodology (T2–T5), and Application (T6–T7).

---

### 1. Skill Attribution (Complete Skill List)

#### T1: Mathematical & Programming Foundations

| Level | Skill |
|:---:|------|
| L0 | Python fundamentals; C++ basics (pointers, memory management, STL); Linux command line and shell scripting; Git version control |
| L1 | Linear algebra (matrix decomposition, eigenvalues, SVD); multivariable calculus (gradients, Jacobian, Hessian); probability and statistics (Bayesian inference, Gaussian distribution, maximum likelihood estimation); fundamentals of ordinary differential equations |
| L2 | Advanced C++ (templates, RAII, move semantics, multithreading); numerical methods (numerical integration, solving linear systems, numerical differentiation); convex optimization fundamentals (LP, QP, duality theory); Python scientific computing ecosystem (NumPy, SciPy, Matplotlib) |
| L3 | Nonlinear optimization (SQP, interior-point methods, IPOPT); Lie groups and Lie algebras (SO(3), SE(3), exponential map); C++ concurrent programming (lock-free data structures, atomic operations, memory ordering); introduction to functional analysis (calculus of variations) |
| L4 | Differential geometry in robotics; advanced numerical optimization (ADMM, stochastic optimization); formal methods fundamentals (temporal logic, introduction to model checking); GPU programming (CUDA basics, parallel computing patterns) |

#### T2: Modeling & Control

| Level | Skill |
|:---:|------|
| L0 | Intuition for rigid-body mechanics (forces, torques, Newton's laws); open-loop vs. closed-loop control concepts |
| L1 | Forward kinematics (DH parameters, homogeneous transformations); inverse kinematics (analytic and numerical methods); Jacobian matrix and velocity mapping; PID control (tuning methods: Ziegler–Nichols); state-space representation (controllability, observability) |
| L2 | Rigid-body dynamics (Newton–Euler recursion, Lagrangian method, Pinocchio/RBDL libraries); LQR (cost function, Riccati equation); EKF/UKF for state estimation (cross-reference with T3); trajectory tracking control (computed torque) |
| L3 | MPC (prediction horizon, constraints, QP solving with OSQP/QP-OASES); impedance and admittance control; operational space control (Khatib 1987); contact dynamics modeling (complementarity constraints, LCP); fundamentals of adaptive control |
| L4 | Whole-Body Control (task priority, null-space projection, QP-based WBC); centroidal dynamics; contact-implicit trajectory optimization; robust control (introduction to H∞); passivity-based control |

#### T3: Perception & State Estimation

| Level | Skill |
|:---:|------|
| L0 | Camera models (pinhole model, distortion); basic image processing (filtering, edge detection); point cloud basics (introduction to PCL) |
| L1 | Feature extraction and matching (ORB, SIFT); stereo vision and depth estimation; IMU principles and pre-integration; sensor calibration (camera intrinsics, hand-eye calibration); point cloud normal estimation (PCA-based k-NN neighborhood covariance analysis); rigid-body transformation fundamentals for registration (optimal rotation via SVD of cross-covariance matrix H = ΣpᵢqᵢᵀT, optimal translation via centroid alignment); basic ICP concept (point-to-point and point-to-plane iterative closest point: alternating correspondence-finding and transformation-update) |
| L2 | Kalman filter family (KF, EKF, UKF); Visual SLAM (ORB-SLAM3: feature extraction, loop closure detection, graph optimization); LiDAR SLAM (LOAM, LIO-SAM); point cloud coarse registration pipeline (FPFH descriptor: 33-dim, fast but prone to feature redundancy in geometrically uniform/planar regions; SHOT descriptor: 352-dim, 3D spatial-grid binning + unique local reference frame (LRF), superior discriminability in feature-poor regions; FLANN approximate nearest-neighbor matching to handle curse of dimensionality for high-dimensional feature spaces; TEASER++ robust global registration: geometric consistency invariant checking, maximum clique inlier selection via PMC, TLS-based decoupled rotation/translation estimation; deterministic and high-outlier-robust vs. RANSAC's probabilistic random sampling — TEASER++ maintains high success rate even at >99% outlier ratio); multi-sensor fusion (IMU+camera, IMU+LiDAR); particle filter |
| L3 | Factor graph optimization (GTSAM/iSAM2); deep learning-based object detection and segmentation (YOLO series, Mask R-CNN); 6DoF object pose estimation; point cloud deep learning (PointNet/PointNet++); Visual-Inertial Odometry (VINS-Mono); GICP fine registration (local surface covariance estimation via k-NN PCA with eigenvalue lower-bound regularization and surface anisotropy modeling: σ_n ≪ σ_t along normal vs. tangent directions; Mahalanobis distance objective E = Σ rᵢᵀ Sᵢ⁻¹ rᵢ where Sᵢ = Σ_q + R Σ_p Rᵀ; Jacobian construction in SE(3) tangent space Jᵢ = [−R[pᵢ]×, I₃] via skew-symmetric operator [p]×; Gauss–Newton normal equations H = JᵀWJ, g = JᵀWr and Levenberg–Marquardt adaptive damping (H + λD)δ = −g with trust-region acceptance criterion; numerical stabilization: Cholesky decomposition for Sᵢ inversion, eigenvalue lower-bound regularization for near-singular surface covariances, M-estimator robust weighting such as Huber/Cauchy/Tukey for outlier-contaminated correspondences) |
| L4 | Vision-Language models (CLIP, SAM2, Grounding DINO); 3D scene understanding (NeRF, 3D Gaussian Splatting); Scene Graphs; BEV perception (primarily for autonomous driving); tactile perception (GelSight, DIGIT sensor processing); open-vocabulary detection |

#### T4: Planning & Decision Making

| Level | Skill |
|:---:|------|
| L0 | Graph search fundamentals (BFS, DFS); configuration space (C-space) concepts |
| L1 | A\*, Dijkstra algorithms; sampling fundamentals (concept of probabilistic completeness); hierarchical decomposition of tasks and actions |
| L2 | Sampling-based motion planning (RRT, PRM, RRT\*, Informed-RRT\*); trajectory optimization (CHOMP, STOMP, direct collocation); MoveIt2 framework usage and configuration; TEB (Timed Elastic Band) planner |
| L3 | Behavior architectures (finite state machines, Behavior Trees / BehaviorTree.CPP); task planning (PDDL, Hierarchical Task Networks / HTN); LLM-based task planning (SayCan, Code-as-Policies, Inner Monologue, JSON Schema, Function Calling); motion primitives (DMP, ProMP) |
| L4 | Multi-robot coordinated planning (task allocation, conflict resolution); TAMP (Task and Motion Planning integration); safety verification (reachability analysis, barrier certificates); online replanning and failure recovery |

#### T5: Robot Learning

| Level | Skill |
|:---:|------|
| L0 | Supervised / unsupervised learning fundamentals; deep learning basics (MLP, CNN, Transformer architecture); basic PyTorch usage |
| L1 | Reinforcement learning fundamentals (MDP, Bellman equation, policy gradient); PPO and SAC implementation and tuning; Gymnasium interface specification; reward function design principles |
| L2 | Imitation learning (Behavior Cloning, DAgger); Action Chunking Transformer (ACT); Domain Randomization (Tobin et al. 2017); teleoperation data collection (leader-follower architecture, data protocols, LeRobot, DexPilot, ALOHA, Open-TeleVision); sim-to-real fundamentals (system identification, action space design, domain gap, digital twin); UMI (Universal Manipulation Interface) |
| L3 | Diffusion Policy (Chi et al. 2023, RSS → IJRR 2024); Flow Matching (Lipman et al. 2023); FAST action tokenizer (DCT frequency-domain compression); teacher-student distillation (privileged information training → sensor policy distillation); data augmentation (image perturbation, action noise); Offline RL (IQL, CQL, AWAC); multi-task learning and task-conditioned policies; 3D Diffusion Policy (Ze et al. 2024, point cloud-conditioned diffusion) |
| L4 | VLA models (RT-2, Octo, OpenVLA, π₀ (monolithic system), π₀.5, Helix, GR00T N1.6, Gemini Robotics); VLA architecture taxonomy ("early fusion vs. dual-system vs. self-correcting (EF-VLA / Helix-GR00T class / closed-loop correction class)"); VLA fine-tuning (SmolVLA, LoRA adaptation, OpenVLA-OFT, π₀-FAST); World Models (Dreamer-v3, TD-MPC2, RWM (ETH, NeurIPS 2025 Outstanding Paper), Gaussian World Model, NVIDIA Cosmos – Cosmos-Predict2.5 (video prediction), Cosmos-Transfer2.5 (controllable world generation), Cosmos-Reason2 (physical reasoning), and Cosmos-RL (reinforcement learning framework)); large-scale data pipelines (Open X-Embodiment, DROID dataset); language-conditioned policies (HULC, language-action alignment); generalist robot policy architectures; VLA post-training (RLHF for robots, GRPO/TGRPO); SmolVLA (Hugging Face, 450M open-source VLA); EF-VLA (ICLR 2025), CoA-VLA (ICCV 2025); Gemini Robotics On-Device (edge deployment version, June 2025); V-JEPA 2 (Meta physical reasoning world model), Runway GWM-1 Robotics |

#### T6: Manipulation (Application Track)

| Level | Skill |
|:---:|------|
| L0 | End-effector types (parallel grippers, vacuum suction cups, overview of dexterous hands); basic grasping concepts (force closure, form closure) |
| L1 | Grasp planning (GraspIt!, analytic grasp synthesis); pick-and-place pipeline (perception → planning → grasping → placing); collision detection and obstacle avoidance |
| L2 | Force/torque control applications (polishing, assembly); bin picking (grasping in cluttered scenes); tool use (tool-frame transformation); introduction to flexible object manipulation |
| L3 | Dexterous manipulation (in-hand object manipulation with multi-finger hands); tactile feedback closed-loop manipulation; contact-rich manipulation (insertion, screwing); learning-based grasping (GraspNet, AnyGrasp) |
| L4 | Language-conditioned manipulation; generalist manipulation policy (cross-task generalization); bimanual cooperative manipulation; deformable object manipulation (cloth, cables); human-robot handover |

#### T7: Locomotion & Navigation (Application Track)

| Level | Skill |
|:---:|------|
| L0 | Mobile robot kinematics (differential drive, omnidirectional wheels); map representations (grid maps, topological maps) |
| L1 | ZMP theory and gait pattern generation (Kajita et al. 2003, historical foundation); LIPM (Linear Inverted Pendulum); path planning (A\*, D\*); localization (AMCL) |
| L2 | Centroidal momentum; RL for locomotion (PPO/SAC/FastTD3 for training humanoid locomotion policies); navigation stack (Nav2 / costmap / planner / controller); large-scale parallel simulation training frameworks (Isaac Gym / Isaac Lab / Genesis); Humanoid-Gym (humanoid robot RL training framework based on NVIDIA Isaac Gym, emphasizing zero-shot sim-to-real transfer) |
| L3 | Dynamic locomotion (running, jumping, stair climbing); terrain adaptation (perception-driven locomotion); sim-to-real for locomotion (teacher-student, ASAP 2025, FastSAC/FastTD3 15-minute training [Seo et al. 2025]); whole-body locomotion control; motion tracking (human motion retargeting to humanoid robots) |
| L4 | Loco-manipulation (locomotion and manipulation synergy, VIRAL [He et al. 2025]); parkour / extreme locomotion capabilities; multi-legged/humanoid whole-body skills (rolling, crawling mode switching); multi-robot navigation (multi-robot cooperative navigation); adversarial locomotion and motion imitation (ALMI, NeurIPS 2025) |

#### T8: Systems Engineering & Infrastructure

| Level | Skill |
|:---:|------|
| L0 | Linux system administration; Docker basics; networking fundamentals (TCP/UDP) |
| L1 | ROS2 fundamentals (nodes, topics, services, actions); URDF/Xacro modeling; introduction to simulation (Gazebo basics, MuJoCo MJCF basics); serial communication (RS-232/485) |
| L2 | Advanced ROS2 (lifecycle nodes, composition, DDS QoS tuning, SROS2, ros2trace, AIMRT, Fast DDS, CycloneDDS); MuJoCo environment setup (Gymnasium wrapper, contact physics tuning, sensor simulation); Genesis simulation platform basics (multi-physics engine, Python API, GPU acceleration); PREEMPT_RT kernel configuration and benchmarking; EtherCAT protocol (IgH master); CAN/CANopen protocol |
| L3 | System architecture patterns (pub-sub, pipeline, request-reply selection, HAL / hardware abstraction layer); Isaac Lab / Isaac Sim (GPU parallel environments, large-scale RL training); safety standards (ISO 10218-1/2, ISO 13849-1, FMEA, hazard analysis); real-time scheduling (priority inversion, priority inheritance, RTOS concepts); ManiSkill/SAPIEN (GPU-parallel manipulation simulation); Newton Physics Engine (NVIDIA + DeepMind + Disney, open-source GPU physics engine); MuJoCo Playground (Zakka et al., 2025) is extensively used in the FastTD3 paper as a GPU-accelerated MuJoCo simulation environment and has become important infrastructure for humanoid locomotion RL research |
| L4 | Complete robotics system architecture design (perception → planning → control → safety, full pipeline); production deployment (OTA updates, monitoring, graceful degradation); AI infrastructure (multimodal data pipelines, MLOps, training cluster management, RDMA, GDR, NVLink, NCCL, MinIO, sherpa-onnx); certification processes (CE/UL/CCC); hard real-time system design (thread priority, global DDS QoS configuration, failure mode analysis); large-scale multi-simulator frameworks (HumanoidVerse: unified training pipeline across IsaacGym/IsaacSim/Genesis) |

---

### 2. Rationale for Skill Layering (L0–L4 Dependency Relationships)

The core logic of the layering is the **knowledge dependency chain**: the skills of L(n) have the skills of L(n–1) as prerequisites.

#### Level Definitions

| Level | Meaning | Analogy |
|:---:|------|------|
| L0 | **Conceptual Awareness**: knows what it is, can use existing tools | Can drive a car but doesn't understand the engine |
| L1 | **Foundational Theory**: understands principles, can implement a simple version from scratch | Understands engine principles, can disassemble and reassemble |
| L2 | **Independent Application**: can work independently on standard problems, can modify existing solutions | Can diagnose common faults and repair them |
| L3 | **Advanced Integration**: can solve non-standard problems, cross-subsystem integration, performance optimization | Can improve engine design |
| L4 | **Architecture & Frontier**: can design complete systems, evaluate and extend cutting-edge methods, mentor others | Can design an entirely new powertrain |

#### Key Dependency Chains per Track

**T2 Modeling & Control:**
L0 → L1 dependency: T1-L1 (linear algebra, calculus) is the prerequisite for forward/inverse kinematics and PID state-space representation.
L1 → L2 dependency: T1-L1 (ordinary differential equations) + T2-L1 (kinematics) are prerequisites for dynamics derivation.
L2 → L3 dependency: T1-L2 (convex optimization/QP) is the prerequisite for MPC; T2-L2 (dynamics) is the prerequisite for impedance control.
L3 → L4 dependency: T1-L3 (nonlinear optimization) + T2-L3 (MPC, impedance control, contact dynamics) are prerequisites for WBC and contact-implicit optimization.

**T3 Perception & State Estimation:**

L0 → L1 dependency: T1-L1 (linear algebra: matrix operations, eigenvalue decomposition) is
the mathematical prerequisite for stereo vision depth estimation and feature matching geometric
verification (essential matrix/fundamental matrix); T1-L1 (linear algebra: SVD, eigenvalue
decomposition) is also the mathematical prerequisite for point cloud normal estimation (PCA via
eigenvalue decomposition of k-NN neighborhood covariance matrix) and optimal rigid-body
transformation solving (optimal rotation R = VUᵀ via SVD of the cross-covariance matrix H,
optimal translation via centroid alignment); T1-L0 (Python/C++ programming) is the programming
prerequisite for OpenCV/PCL implementation.

L1 → L2 dependency: T1-L1 (probability theory: Bayesian estimation, Gaussian distribution) +
T3-L1 (IMU principles, sensor calibration) are prerequisites for the Kalman filter family and
multi-sensor fusion; T3-L1 (feature extraction and matching) + T1-L1 (linear algebra: SVD) are
prerequisites for the Visual SLAM front-end (feature tracking, epipolar geometry); T3-L1 (point
cloud normal estimation, basic ICP concept) + T1-L1 (linear algebra: eigenvalue decomposition
for unique local reference frame construction) are prerequisites for the SHOT descriptor (3D
spatial-grid binning requires a geometrically consistent LRF; the 352-dim vector encodes
anisotropic neighborhood geometry) and the TEASER++ coarse registration pipeline (geometric
consistency invariant checking requires understanding of rigid-body distance invariants under
transformation; maximum clique inlier selection requires familiarity with graph-theoretic
combinatorial reasoning as a deterministic alternative to RANSAC's probabilistic sampling).

L2 → L3 dependency: T1-L2 (numerical methods, convex optimization fundamentals) is the
prerequisite for factor graph optimization (nonlinear least squares in GTSAM); T5-L0 (deep
learning basics: CNN) is the prerequisite for object detection (YOLO series), segmentation (Mask
R-CNN), and point cloud deep learning (PointNet/PointNet++); T3-L2 (SLAM, multi-sensor fusion)
is the prerequisite for VIO (VINS-Mono); T3-L2 (point cloud coarse registration: TEASER++
inlier correspondence set serves as a reliable initialization for local fine registration) +
T1-L2 (numerical methods: linear system solving, Cholesky decomposition for positive-definite
matrices) + T1-L3 (Lie groups and Lie algebras: SO(3)/SE(3) parameterization, exponential map,
tangent-space Jacobian construction via skew-symmetric operator [p]×) + T1-L2 (convex
optimization: understanding Levenberg–Marquardt as trust-region interpolation between
Gauss–Newton and gradient descent) are prerequisites for GICP fine registration
(covariance-weighted Mahalanobis distance objective E = Σ rᵢᵀ Sᵢ⁻¹ rᵢ with Sᵢ = Σ_q + R Σ_p
Rᵀ; tangent-space Jacobian Jᵢ = [−R[pᵢ]×, I₃]; LM adaptive damping (H + λD)δ = −g with
accept/reject trust-region criterion; eigenvalue lower-bound regularization and Cholesky
decomposition for numerically stable Sᵢ inversion).

L3 → L4 dependency: T5-L0 (Transformer architecture) + T3-L3 (object detection and segmentation, point cloud deep learning) are prerequisites for Vision-Language models (CLIP, SAM2, Grounding DINO); T3-L3 (6DoF pose estimation) + T1-L3 (nonlinear optimization) are prerequisites for NeRF/3D Gaussian Splatting scene reconstruction; T3-L3 (deep learning perception) is the prerequisite for BEV perception and open-vocabulary detection.

**T4 Planning & Decision Making:**

L0 → L1 dependency: T1-L0 (Python programming, basic data structures) is the prerequisite for implementing graph search algorithms; T4-L0 (C-space concept) is the conceptual prerequisite for understanding probabilistic completeness in sampling-based planning.

L1 → L2 dependency: T1-L1 (probability theory: sampling theory) + T4-L1 (A\*, sampling concepts) are prerequisites for the RRT/PRM family of algorithms; T2-L1 (forward/inverse kinematics) is the prerequisite for mapping C-space planning to joint-space execution; T1-L2 (convex optimization: QP) is the prerequisite for trajectory optimization (cost function minimization in CHOMP/STOMP).

L2 → L3 dependency: T4-L2 (sampling-based planning, trajectory optimization, MoveIt2) + software engineering experience are prerequisites for behavior architecture system design (state machines, Behavior Trees); T5-L0 (deep learning basics) + NLP fundamentals are prerequisites for LLM-based task planning (SayCan, Code-as-Policies); T2-L2 (dynamics) + T4-L2 (trajectory optimization) are prerequisites for motion primitives (DMP, ProMP).

L3 → L4 dependency: T4-L3 (task planning PDDL/HTN) + T4-L2 (motion planning) are prerequisites for TAMP integration; T4-L3 (behavior architectures) + T2-L3 (MPC) are prerequisites for online replanning and failure recovery; T1-L3 (nonlinear optimization, introduction to formal methods) is the prerequisite for safety verification (barrier certificates, reachability analysis).

**T5 Robot Learning:**

L0 → L1 dependency: T1-L1 (probability theory: probabilistic transitions in MDPs, expected returns; calculus: derivatives for policy gradients) + T5-L0 (deep learning basics: MLP/CNN as policy and value function networks, PyTorch implementation) are prerequisites for RL theory and PPO/SAC implementation.

L1 → L2 dependency: T5-L1 (RL fundamentals) + T8-L1 (introduction to simulation: Gazebo/MuJoCo) are prerequisites for sim-to-real fundamentals; T5-L0 (supervised learning) + T8-L1 (ROS2: data flow interfaces) are prerequisites for imitation learning (BC, DAgger) and teleoperation data collection (DexPilot, ALOHA, Open-TeleVision); T5-L1 (reward function design) + T8-L2 (MuJoCo environment setup) are prerequisites for domain randomization and digital twin experiments.

L2 → L3 dependency: T5-L2 (imitation learning, domain randomization) + T1-L2 (convex optimization fundamentals: understanding loss functions in probabilistic distribution modeling) are prerequisites for Diffusion Policy and Flow Matching theory; T5-L2 (sim-to-real fundamentals) + T8-L2/L3 (GPU-parallel simulation) are prerequisites for large-scale teacher-student distillation training; T5-L1 (RL: off-policy methods) is the prerequisite for Offline RL (IQL, CQL, AWAC).

L3 → L4 dependency: T5-L3 (Diffusion Policy / Flow Matching as action decoder) + T3-L4 (Vision-Language models: CLIP/SigLIP as visual encoder) + T5-L0 (Transformer architecture as LLM backbone) are prerequisites for understanding and training VLA models; T5-L3 (teacher-student distillation) + T5-L1 (RL: PPO) + T8-L3 (large-scale simulation) are prerequisites for World Model training (Dreamer-v3, RWM); T5-L3 (multi-task learning) + large-scale data engineering experience are prerequisites for generalist robot policies and large-scale data pipelines.

**T6 Manipulation:**

L0 → L1 dependency: T2-L1 (forward/inverse kinematics: end-effector pose computation) + T3-L0 (camera model: for visually guided grasping) + T4-L1 (A\*/planning basics: spatial reasoning for collision detection) are prerequisites for grasp planning and the pick-and-place pipeline.

L1 → L2 dependency: T2-L2 (rigid-body dynamics: understanding contact forces and friction) + T2-L1 (Jacobian: force/velocity mapping) + T6-L1 (grasp planning basics) are prerequisites for force/torque control applications (force-position hybrid control in polishing and assembly); T3-L1/L2 (depth perception, point cloud processing) are prerequisites for bin picking.

L2 → L3 dependency: T2-L3 (impedance/admittance control, contact dynamics modeling) is the prerequisite for contact-rich manipulation (insertion, screwing); T3-L3 (6DoF pose estimation, point cloud deep learning) + T5-L2/L3 (imitation learning, Diffusion Policy) are prerequisites for learning-based grasping (GraspNet, AnyGrasp); T3-L4 (tactile sensor processing) + T2-L3 (impedance control) are prerequisites for tactile feedback closed-loop manipulation.

L3 → L4 dependency: T5-L3/L4 (Diffusion Policy, VLA models: language-conditioned action generation) + T6-L3 (dexterous manipulation, tactile closed-loop) are prerequisites for language-conditioned manipulation and generalist manipulation policies; T6-L3 (multi-finger dexterous manipulation) + T2-L4 (bimanual coordination in whole-body control) are prerequisites for bimanual cooperative manipulation; T5-L2/L3 (imitation learning, data augmentation) + T3-L3/L4 (perceptual generalization) are prerequisites for deformable object manipulation.

**T7 Locomotion & Navigation:**

L0 → L1 dependency: T2-L1 (kinematics: joint-to-end-effector mapping) + T4-L1 (path planning A\*/D\*) + T1-L1 (linear algebra) are prerequisites for ZMP theory and path planning implementation.

L1 → L2 dependency: T2-L2 (rigid-body dynamics: Newton–Euler recursion) is the prerequisite for centroidal momentum derivation; T5-L1 (RL: PPO/SAC) + T8-L1/L2 (MuJoCo environment, Isaac Gym/Genesis) are prerequisites for RL for locomotion training; T3-L2 (SLAM) + T4-L2 (sampling-based planning, TEB planner) are prerequisites for navigation stack (Nav2) configuration.

L2 → L3 dependency: T7-L2 (RL locomotion policy, centroidal dynamics) + T5-L2 (sim-to-real fundamentals: domain randomization) + T8-L2/L3 (large-scale parallel simulation: Isaac Lab/Genesis) are prerequisites for dynamic locomotion (running, jumping) and sim-to-real for locomotion (teacher-student distillation, ASAP); T3-L2/L3 (perception: depth estimation, SLAM) + T7-L2 (RL locomotion) are prerequisites for terrain-adaptive perception-driven locomotion; T2-L4 (whole-body control) + T7-L2 (RL locomotion) are prerequisites for whole-body locomotion control.

L3 → L4 dependency: T7-L3 (dynamic locomotion, whole-body control) + T6-L2/L3 (force-controlled manipulation, dexterous manipulation foundational skills) are prerequisites for loco-manipulation (VIRAL); T7-L3 (dynamic locomotion, sim-to-real) + T5-L3 (teacher-student, motion primitives) are prerequisites for parkour/extreme locomotion; T5-L3 (adversarial learning, motion imitation) + T7-L3 (whole-body locomotion) are prerequisites for ALMI-style adversarial locomotion and motion imitation.

---

### 3. Cross-Track Application / System Mapping

The following analyzes how five key systems are composed from the skills across Tracks, and examines the inter-Track dependency relationships.

---

### 3.1 VLA (Vision-Language-Action) System

**System Definition:** VLA is a class of multimodal foundation models that, given images (or video) of the robot's surroundings and natural language instructions, directly output executable low-level robot actions. VLAs are typically constructed by fine-tuning a VLM on large-scale "visual observation + language instruction → robot trajectory" datasets, and comprise a visual-language encoder (ViT) that maps images and language to a latent space, and an action decoder that converts latent representations into continuous action outputs.

**Relevant Tracks and Level Mapping:**

| Core Capability | Primary Track | Key Skills (Level) |
|----------|-----------|-----------------|
| Visual Encoding | T3 Perception | Camera model (L0) → deep learning detection/segmentation (L3) → VL models CLIP/SigLIP (L4) |
| Language Understanding | T5 Learning | Transformer architecture (L0) → LLM fundamentals → VLM pre-training understanding |
| Action Generation | T5 Learning | Imitation learning BC (L2) → Diffusion Policy/Flow Matching (L3) → VLA action head (L4) |
| Action Tokenization | T5 Learning | FAST DCT frequency-domain compression (L3) → discrete vs. continuous action representations (L4) |
| Architecture Design | T5 Learning | Early fusion / dual-system / self-correcting three paradigms (L4) |
| Data Pipeline | T8 Systems | Teleoperation collection (T5-L2) → Open X-Embodiment/DROID (T5-L4) → MLOps (T8-L4) |
| Fine-tuning & Deployment | T5 + T8 | LoRA/OFT adaptation (L4) → FSDP distributed training → edge inference (Gemini On-Device) |
| Post-training Alignment | T5 Learning | RLHF for robots → GRPO/TGRPO (L4) |

**Representative Systems and Architecture Classification:**

Current VLA models have converged toward three major architectural paradigms:

(1) **Early Fusion:** Exemplified by EF-VLA (ICLR 2025), which preserves the semantic consistency of CLIP pre-training by fusing image-text embeddings in the early stages of the Transformer backbone. RT-2 and OpenVLA also belong to this category (monolithic end-to-end).

(2) **Dual-System:** Exemplified by GR00T N1 and Helix, where System 1 is a fast diffusion/flow-matching policy (10ms latency) and System 2 is an LLM for task planning and high-level sequencing. This decoupled architecture achieves both broad generalization and fast low-level control.

(3) **Self-Correcting:** Includes agentic VLA frameworks where an LLM planner validates and replans actions through uncertainty-driven feedback. CoA-VLA (ICCV 2025) achieves closed-loop error correction through chain-of-affordance reasoning.

**Typical Skill Path (from zero to VLA researcher):**
T1-L0/L1 (programming + mathematics) → T5-L0 (DL basics/PyTorch) → T3-L0/L1 (vision basics) → T5-L1 (RL fundamentals) → T5-L2 (imitation learning/teleoperation/LeRobot) → T8-L1/L2 (simulation environment setup) → T5-L3 (Diffusion Policy/Flow Matching) → T3-L4 (VL models) → T5-L4 (VLA training/fine-tuning/post-training)

### 3.2 World Model

**System Definition:** A world model is a class of AI system that builds an internal representation of the environment and uses it to simulate future events within that environment. In robotics, world models allow policies to be trained in "imagination," without real-world interaction.

**Relevant Tracks and Level Mapping:**

| Core Capability | Primary Track | Key Skills (Level) |
|----------|-----------|-----------------|
| Dynamics Modeling | T2 Control | Rigid-body dynamics (L2) → contact dynamics (L3) → contact-implicit optimization (L4) |
| Visual Prediction | T3 Perception | Image processing (L0) → deep learning (L3) → NeRF/3DGS (L4) |
| Sequence Modeling | T5 Learning | Transformer (L0) → RL (L1) → Dreamer-v3/TD-MPC2 (L4) → RWM (L4) |
| 3D Representation | T3 Perception | Point clouds (L0/L3) → 3DGS (L4) → GWM Gaussian World Model (T5-L4) |
| Video Generation | T5 Learning | Diffusion model fundamentals → video prediction models → Cosmos Predict (T5-L4) |
| Simulation Infrastructure | T8 Systems | MuJoCo (L1) → Isaac Lab (L3) → Cosmos platform (L4) |
| Policy Optimization | T5 Learning | PPO (L1) → model-based RL (L4) → imagination-based training |

**Key System Instances:**

(1) **State-Space World Model:** RWM (ETH Zurich) is a black-box neural network simulator that autoregressively predicts future robot observations using a GRU with a dual-autoregressive mechanism for stable long-horizon prediction. Because RWM predicts a stochastic distribution of observations, each imagined rollout naturally introduces diverse dynamics, equivalent to free domain randomization.

(2) **3D Gaussian World Model:** GWM (ICCV 2025) performs efficient dynamic modeling based on a Gaussian diffusion Transformer and Gaussian VAE, predicting future states in a 3D Gaussian representation, supporting action-conditioned 3D video prediction and model-based RL.

(3) **Video Prediction World Model:** NVIDIA Cosmos WFM is a suite of physically-aware video generation models trained on 90 quadrillion tokens (20 million hours of real-world data). Cosmos Reason has spatiotemporal awareness and uses chain-of-thought reasoning to understand video data and predict interaction outcomes, and can be used to build high-level planners for VLAs.

(4) **General-Purpose World Model:** Runway GWM-1 is an autoregressive model based on Gen-4.5 that generates frame by frame, runs in real time, and can be interactively controlled via actions (camera pose, robot commands), including a GWM Robotics variant.

**Typical Skill Path (from zero to World Model researcher):**
T1-L0/L1 (programming + mathematics) → T5-L0 (DL/PyTorch) → T5-L1 (RL fundamentals/MDP) → T2-L1/L2 (kinematics/dynamics: understanding physical state transitions) → T8-L1/L2 (MuJoCo simulation) → T5-L3 (diffusion models/Flow Matching) → T3-L4 (NeRF/3DGS: 3D representation learning) → T5-L4 (World Model training: Dreamer → RWM → Cosmos fine-tuning) → T8-L3/L4 (large-scale training infrastructure)

### 3.3 Robotic Manipulation System

**System Definition:** A robotic manipulation system integrates perception, planning, control, and learning into a complete manipulation pipeline, enabling robots to grasp, place, assemble, and manipulate various objects in unstructured environments.

**Relevant Tracks and Level Mapping:**

| Core Capability | Primary Track | Key Skills (Level) |
|----------|-----------|-----------------|
| Kinematics / Dynamics | T2 Control | Forward/inverse kinematics (L1) → dynamics (L2) → impedance control (L3) → WBC (L4) |
| Force Control | T2 Control | PID (L1) → computed torque (L2) → impedance/admittance control (L3) |
| Object Perception | T3 Perception | Camera calibration (L1) → point cloud coarse registration / TEASER++ (L2) → 6DoF pose estimation / GICP (L3) → open-vocabulary detection (L4) |
| Tactile Perception | T3 Perception | Tactile sensor processing GelSight/DIGIT (L4) |
| Grasp Planning | T6 Manipulation | Force closure (L0) → GraspIt! (L1) → AnyGrasp (L3) → learning-based (L3) |
| Motion Planning | T4 Planning | A\* (L1) → RRT\* (L2) → TAMP (L4) |
| Policy Learning | T5 Learning | BC (L2) → ACT/Diffusion Policy (L3) → VLA (L4) |
| System Integration | T8 Systems | ROS2 (L1) → MoveIt2 (T4-L2) → full-stack architecture (L4) |

**Typical Manipulation Pipeline Architectures:**

**Classical Pipeline:** Perception (T3-L2/L3: object detection + pose estimation) → grasp planning (T6-L1/L3: GraspNet) → motion planning (T4-L2: MoveIt2/RRT\*) → force-controlled execution (T2-L3: impedance control) → state monitoring (T3-L1: force sensor feedback)

**Learning-based Pipeline:** Data collection (T5-L2: teleoperation/LeRobot/UMI) → Diffusion Policy as a CNN-based visuomotor policy, generating only action trajectories (distinct from Diffuser's joint state-action denoising) → deployment (T8-L2/L3: real-time inference)

**End-to-End Pipeline:** Uses a VLA to predict coarse actions, then a diffusion model policy to refine actions for increased precision and cross-platform adaptability (e.g., TinyVLA + Diffusion Head)

**Typical Skill Path (manipulation system engineer):**
T1-L0/L1 (programming + mathematics) → T2-L1 (kinematics) → T8-L1 (ROS2/URDF) → T3-L0/L1 (vision basics/calibration) → T4-L2 (MoveIt2 motion planning) → T6-L1/L2 (grasping + force control) → T5-L2 (imitation learning) → T2-L3 (impedance control) → T6-L3 (dexterous manipulation/tactile closed-loop) → T5-L3/L4 (Diffusion Policy/VLA deployment)

### 3.4 Humanoid Locomotion System

**System Definition:** A humanoid locomotion system enables bipedal robots to achieve stable, agile, and adaptive locomotion across diverse terrains. The current mainstream approach centers on large-scale parallel simulation + reinforcement learning + sim-to-real transfer.

**Relevant Tracks and Level Mapping:**

| Core Capability | Primary Track | Key Skills (Level) |
|----------|-----------|-----------------|
| Dynamics Modeling | T2 Control | Rigid-body dynamics (L2) → centroidal dynamics (L4) → contact dynamics (L3) |
| Whole-Body Control | T2 Control | LQR (L2) → MPC (L3) → QP-based WBC (L4) |
| RL Training | T5 Learning | PPO/SAC (L1) → large-scale parallel training (L2/T7-L2) → FastSAC/FastTD3 (T7-L3) |
| Sim-to-Real | T5 + T8 | Domain Randomization (L2) → teacher-student distillation (L3) → ASAP (T7-L3) |
| Motion Tracking | T7 Locomotion | Human motion retargeting → motion imitation policy (L3) → ALMI adversarial (L4) |
| Perception-Driven | T3 Perception | Depth estimation (L1) → height maps (L2/L3) → visual policy distillation (VIRAL, T7-L4) |
| Simulation Platform | T8 Systems | MuJoCo (L1) → Isaac Gym/Lab (L3) → Genesis (L2) → HumanoidVerse (L4) |

**Current Technical Paradigms and Evolution:**

(1) **Classical Control Route (Historical Foundation):** ZMP gait pattern generation → centroidal dynamics → real-time WBC/MPC solving. This route has deep roots in industry (e.g., early Boston Dynamics), but has limited generalization capability.

(2) **RL End-to-End Route (Current Mainstream):** Through carefully designed hyperparameters and reward functions, FastSAC/FastTD3 can scale to full-body humanoid control, completing training in 15 minutes on a single RTX 4090 (with randomized dynamics, rough terrain, and push perturbations). This reduces humanoid sim-to-real iteration time to the minute scale.

(3) **Teacher-Student Distillation Route:** VIRAL uses privileged RL teacher → visual student policy distillation, bridging the sim-to-real gap through large-scale visual domain randomization (lighting, materials, camera parameters, etc.). Computational scale is critical (requires scaling to tens of GPUs).

(4) **Adversarial Whole-Body Locomotion Route:** ALMI decouples the upper and lower body into adversarial policies—the lower body provides robust locomotion following velocity commands, and the upper body tracks various motions—achieving coordinated whole-body control through iterative updates, validated on the Unitree H1-2.

**Typical Skill Path (humanoid locomotion researcher):**
T1-L0/L1/L2 (programming + mathematics + numerical methods) → T2-L1/L2 (kinematics/dynamics) → T5-L0/L1 (DL/RL fundamentals) → T8-L1/L2 (MuJoCo/Isaac Gym environment) → T7-L1/L2 (centroidal dynamics/RL locomotion) → T5-L2 (domain randomization/sim-to-real) → T7-L3 (dynamic locomotion/teacher-student/ASAP) → T2-L4 (WBC) → T7-L4 (loco-manipulation/ALMI)

### 3.5 Multimodal Reasoning System

**System Definition:** A multimodal reasoning system enables robots to integrate multimodal inputs—visual, language, haptic, and others—for semantic understanding, physical reasoning, and task planning, providing high-level cognitive capabilities for VLAs and world models.

**Relevant Tracks and Level Mapping:**

| Core Capability | Primary Track | Key Skills (Level) |
|----------|-----------|-----------------|
| Visual Understanding | T3 Perception | Image processing (L0) → object detection/segmentation (L3) → VL models/scene graphs (L4) |
| Language Interface | T4 Planning | LLM-based task planning (L3) → Code-as-Policies (L3) → VLA integration (T5-L4) |
| Physical Reasoning | T5 + T2 | Dynamics modeling (T2-L2) → World Model (T5-L4) → Cosmos Reason (T5-L4) |
| Spatial Reasoning | T3 + T4 | 3D scene understanding (T3-L4) → scene graphs (T3-L4) → BEV perception (T3-L4) |
| Affordance Reasoning | T6 + T3 | Grasping (T6-L0) → pose estimation (T3-L3) → open-vocabulary detection (T3-L4) → CoA-VLA |
| Task Decomposition | T4 Planning | Hierarchical decomposition (L1) → PDDL/HTN (L3) → TAMP (L4) |
| Chain-of-Thought Reasoning | T5 Learning | Transformer (L0) → LLM reasoning → Cosmos Reason uses chain-of-thought reasoning to understand video and predict physical interaction outcomes |

**Key System Instances and Technical Evolution:**

(1) **LLM as High-Level Planner:** SayCan (Google, 2022) combines the LLM's task knowledge with the feasibility assessment of value functions; Code-as-Policies uses code as a policy representation; Inner Monologue introduces internal dialogue for closed-loop error correction. All of these fall at the T4-L3 level.

(2) **VLM as Semantic Interface:** In dual-system VLAs, System 2 (the VLM in systems such as Helix and GR00T N1) is responsible for scene understanding and language understanding, passing high-level semantic representations to System 1. GR00T N1.6 further enhances reasoning capabilities, enabling decomposition of complex instructions and exploitation of commonsense knowledge.

(3) **Physical Reasoning WFM:** Cosmos Reason is an open, customizable WFM with spatiotemporal awareness. Developers can use it to improve data annotation and curation, enhance existing world foundation models, or create new VLAs.

(4) **Chain-of-Affordance Reasoning:** CoA-VLA (ICCV 2025) introduces chain-of-thought reasoning into VLAs through four types of affordance, modeling robot affordances as intermediate outputs in natural language format.

**Typical Skill Path (multimodal reasoning researcher):**
T1-L0/L1 (programming + mathematics) → T5-L0 (DL/Transformer) → T3-L0/L1/L3 (vision → detection/segmentation) → T4-L1/L3 (planning basics → LLM planning) → T3-L4 (VL models/scene graphs/open vocabulary) → T5-L4 (VLA/World Model) → multimodal reasoning integration (Cosmos Reason / CoA-VLA / GR00T N1.6)