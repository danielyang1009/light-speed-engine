# Volume 34, Issue 03
- March 1988
- Pages 263-429
- David Simchi-Levi

## 1. The Design, Analysis and Implementation of Heuristics
### Author(s):
- Marshall L. Fisher
- Alexander H. G. Rinnooy Kan
### Published:
- 1 Mar 1988
### Abstract:
The 1950s were a flourishing period for Management Science that saw many practical successfully attacked through the application of inelegant but effective heuristics. In the 1960s, attention turned to optimization, leading to the development of algorithms that employed more sophisticated mathematical constructs. While these algorithms were a significant research achievement, they failed to provide for reliable solutions to many problems. The 1970s seem to have been a period of soul searching in which computational complexity results were discovered, providing evidence that those who failed to develop effective optimization algorithms should not be discouraged, since the problems were probably intractable anyway. As a consequence, some of the intellectual energy that had been devoted to optimization began to be directed to the study of heuristics, but from an enriched perspective that emphasized theoretical performance analysis, both worth case and probabilistic.
### Link:
- https://doi.org/10.1287/mnsc.34.3.263

## 2. Asymptotic Methods in the Probabilistic Analysis of Sequencing and Packing Heuristics
### Author(s):
- E. G. Coffman, Jr.
- G. S. Lueker
- A. H. G. Rinnooy Kan
### Published:
- 1 Mar 1988
### Abstract:
Recently there has been considerable interest in the average-case performance of heuristics. This paper pursues that interest, where it concerns sequencing and packing problems. In particular, we survey the methods that have been used to obtain formal probabilistic analyses of heuristics for makespan scheduling and one-dimensional bin packing. In so doing, we present many of the key results in these research areas.
### Link:
- https://doi.org/10.1287/mnsc.34.3.266

## 3. Heuristics Based on Spacefilling Curves for Combinatorial Problems in Euclidean Space
### Author(s):
- John J. Bartholdi, III
- Loren K. Platzman
### Published:
- 1 Mar 1988
### Abstract:
We describe a family of heuristics to solve combinatorial problems such as routing and partitioning. These heuristics exploit geometry but ignore specific distance measures. Consequently they are simple and fast, but nonetheless fairly accurate, and so seem well-suited to operational problems where time or computing resources are limited. We survey promising new application areas, and show how procedures may be customized to reflect the structure of particular applications.
### Link:
- https://doi.org/10.1287/mnsc.34.3.291

## 4. Minimum Spillage Sequencing
### Author(s):
- Craig A. Tovey
- Gideon Weiss
- James R. Wilson
### Published:
- 1 Mar 1988
### Abstract:
The minimum spillage sequencing problem, which arises in real-time satellite signal data processing, requires a set of numbers to be arranged so as to minimize the overflow of the partial sums above an upper bound. We subject several heuristics to worst-case analysis, average-case analysis, and computational testing. The results demonstrate that the problem, though NP-hard, can be handled effectively. One of the highlights of the analysis is a tight upper bound on the fraction of overflow when the problem is solved to optimality, together with an O(n log n) safe heuristic which never exceeds this bound.
### Link:
- https://doi.org/10.1287/mnsc.34.3.306

## 5. Heuristics with Constant Error Guarantees for the Design of Tree Networks
### Author(s):
- Kemal Altinkemer
- Bezalel Gavish
### Published:
- 1 Mar 1988
### Abstract:
A tree network is a collection of trees rooted at a common central node. Several types of network design problems can be viewed as requiring the formation of a spanning tree network of minimum length, subject to a bound on the sum of weights on the nodes of any component tree. Such problems are NP-complete, and experience has shown that only small examples can be solved to optimality. This paper describes an efficient heuristic algorithm based on partitioning of a traveling salesman tour. When all the nodes have a unit weight and the bound is K, the heuristic finds a solution whose cost is at most 3  2/K times the minimum; in the general case the error bound is 4.
### Link:
- https://doi.org/10.1287/mnsc.34.3.331

## 6. Finding Embedded Network Rows in Linear Programs I. Extraction Heuristics
### Author(s):
- Robert E. Bixby
- Robert Fourer
### Published:
- 1 Mar 1988
### Abstract:
An embedded network within a linear program is, roughly speaking, a subset of constraints that represent conservation of flow. We examine three broad classes of heuristic techniquesrow-scanning deletion, column-scanning deletion, and row-scanning additionfor the extraction of large embedded networks. We present a variety of implementations, and compare their performance on realistic test problems. The success of our tests depends, in part, on several preprocessing steps that scale the constraint matrix and that set aside certain rows and columns. Efficiency of the subsequent network extraction is dependent on the implementation, in predictable ways. Effectiveness is harder to explain; the more sophisticated and expensive implementations seem to be most reliable, but much simpler implementations sometimes find larger networks. The largest networks are obtained by applying a final augmentation phase, which is studied in the second part of this paper.
### Link:
- https://doi.org/10.1287/mnsc.34.3.342

## 7. A Heuristic Scheduling Policy for Multi-Item, Single-Machine Production Systems with Time-Varying, Stochastic Demands
### Author(s):
- Robert C. Leachman
- Andr Gascon
### Published:
- 1 Mar 1988
### Abstract:
A heuristic scheduling policy is introduced for multi-item, single-machine production systems facing stochastic, time-varying demands. The policy, which we term the dynamic cycle lengths heuristic, integrates feedback control based on the monitoring of inventory levels with the maintenance of economic production cycles. The policy is applied time period by time period to make decisions concerning which items to produce in what quantities during the next time period. These quantities reflect production cycles revised each time period in response to differences between projected and actual inventory levels and in response to changes in demand rates. We extend the basic scheduling policy in order to integrate its use with tactical planning. We also discuss the results of simulation tests of the heuristic against other scheduling policies.
### Link:
- https://doi.org/10.1287/mnsc.34.3.377

## 8. The Shifting Bottleneck Procedure for Job Shop Scheduling
### Author(s):
- Joseph Adams
- Egon Balas
- Daniel Zawack
### Published:
- 1 Mar 1988
### Abstract:
We describe an approximation method for solving the minimum makespan problem of job shop scheduling. It sequences the machines one by one, successively, taking each time the machine identified as a bottleneck among the machines not yet sequenced. Every time after a new machine is sequenced, all previously established sequences are locally reoptimized. Both the bottleneck identification and the local reoptimization procedures are based on repeatedly solving certain one-machine scheduling problems. Besides this straight version of the Shifting Bottleneck Procedure, we have also implemented a version that applies the procedure to the nodes of a partial search tree. Computational testing shows that our approach yields consistently better results than other procedures discussed in the literature. A high point of our computational testing occurred when the enumerative version of the Shifting Bottleneck Procedure found in a little over five minutes an optimal schedule to a notorious ten machines/ten jobs problem on which many algorithms have been run for hours without finding an optimal solution.
### Link:
- https://doi.org/10.1287/mnsc.34.3.391

## 9. NoteAn Approximate Algorithm for Multidimensional Zero-One Knapsack ProblemsA Parametric Approach
### Author(s):
- Jae Sik Lee
- Monique Guignard
### Published:
- 1 Mar 1988
### Abstract:
A new approximate algorithm for multidimensional zero-one knapsack problems with all positive coefficients is presented. The procedure is controlled by three parameters which affect the tradeoff between solution quality and computation time and whose values are set by the users. For 48 test problems with 5 to 20 constraints and 6 to 500 variables, the solution found was on the average within 0.34% of the optimum and the computation time was the shortest compared with three other well-known heuristics.
### Link:
- https://doi.org/10.1287/mnsc.34.3.402

## 10. Piecewise-Linear Approximation Methods for Nonseparable Convex Optimization
### Author(s):
- B. Feijoo
- R. R. Meyer
### Published:
- 1 Mar 1988
### Abstract:
An algorithm is described for the solution of nonseparable convex optimization problems. This method utilizes iterative piecewise-linear approximation of the nonseparable objective function, but requires function values only along a translated set of axes, thereby avoiding the curse of dimensionality commonly associated with grid methods for multi-dimensional problems. A global convergence proof is given under the assumptions that the objective function is Lipschitz continuous and differentiable and that the feasible set is convex and compact. The method is well-suited to linearly constrained large-scale optimization, since the direction-finding problems reduce to linear programs of manageable size. It is particularly appropriate for nonlinear networks, since it preserves the network structure of the constraints. In addition, because the resulting objective function approximation is separable, this approach permits for certain problem classes a decomposition that may be exploited for parallel computation. Some numerical results on the CRYSTAL multicomputer are presented to illustrate this decomposition feature.
### Link:
- https://doi.org/10.1287/mnsc.34.3.411

## 11. An O(T2) Algorithm for the NI/G/NI/ND Capacitated Lot Size Problem
### Author(s):
- Chia-Shin Chung
- Chien-Hua Mike Lin
### Published:
- 1 Mar 1988
### Abstract:
In this paper, we study a class of the capacitated dynamic lot size problem, where, over time, the setup costs are nonincreasing, the unit holding costs have arbitrary pattern, the unit production costs are nonincreasing and the capacities are nondecreasing. We investigate the properties of the optimal solution for the problem and develop the concept of candidate subplan. It is proven that only the candidate subplans need to be examined in searching for an optimal solution. A dynamic programming algorithm, incorporating the concept of candidate subplan, is then devised which has run time complexity of O(T2).
### Link:
- https://doi.org/10.1287/mnsc.34.3.420

## 12. About Authors
### Author(s):
### Published:
- 1 Mar 1988
### Abstract:
None
### Link:
- https://doi.org/10.1287/mnsc.34.3.427

