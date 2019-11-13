# Abstract

Railway networks are of great importance for every economy. Thus, it is all the more important to understand the reasons why and how they can fail. Yet, due to the size and complexity, their susceptibility to failures is not completely understood. This research project investigates the vulnerability of the Swiss railway network using network scientific models. [2]

# Introduction

Railway systems need to perform well even under suboptimal circumstances. Cascade delays and cancellations are daily challenges for both passengers and railway companies. [2] Existing research showed that the network topology has an effect on the performance of a railway system. [5] More recently (2018), the authors of [2] analyzed the resilience and robustness of a UK railway network. They showed that poor performance correlates more with cascade effects that failures. [2]

Needless to say, the are many reasons why railway systems can fail. For this reason, the focus of this study is the Swiss railway system for which only few studies exist. In 2008, the authors of [1] published a graph-theoretical analysis of the Swiss railway network over time. They've used measures such as degree/betweenness centrality to characterise the growth of the Railway network [1]. However, they've suggested further research to explain the robustness of the network. In 2009, the authors of [6] proposed a generalized linear model (GLM) to assess the vulnerability of the Swiss road network. The downside of their approach is that they assumed the failures to be mutually exclusive [6]. 

This research projects extends [1] and [6] by using network scientific models. The primary focus is to analyze the Swiss railway network regarding graph characteristics and vulnerabilities.

## Transport networks

Transport networks are essential for people and economy. Early research on transport networks focused on geometric and topological properties. Later, with the availability of computational power, the research shifted towards network structures. [1] Recently, papers such as [2] and [7] used graph properties to model robustness and delay dynamics.

There are several differences to other networks such as social networks. Transport networks represent real objects such as lines and railway stations. These physical objects have constraints themselves which influences the degree distribution. Additionally, monetary constraints apply as well, thus restrict the ability for them to be scale-free. [1] 

## The Swiss railway network

According to the "European Railway Performance Index", Switzerland has one of the best performing railways [4]. Yet, the increased load over the past years is a constant challenge. Every delay or cancellation might result in cascade failures.

Every railway network is slightly different. This is due to their history and how they grew over the years. The Swiss railway network is special because its early growth was purely driven by economic values. This means that cities were prioritized and urban areas were not considered in the planning process. Moreover, due to competition of private companies, the networks grew more or less independent of each other. Today, most railways belong to the Swiss Federal Railways (SBB). [1]

# References

1 Graph-Theoretical Analysis of the Swiss Road and Railway Networks Over Time 

2 Resilience or Robustness: Identifying Topological Vulnerabilities in Rail Networks 

3 https://www.20min.ch/schweiz/news/story/-Verspaetungen-nehmen-zu--weil-SBB-am-Limit-ist--25925140

4 https://www.bcg.com/en-ch/publications/2017/transportation-travel-tourism-2017-european-railway-performance-index.aspx

5 Complex Network Topology of Transportation Systems 

6 Vulnerability Assessment Methodology for Swiss Road Network

7 Complex delay dynamics on railway networks from universal laws to realistic modelling