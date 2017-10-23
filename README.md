![](https://github.com/mm-wang/metashape/blob/master/Documentation/5%20Live%20Demo/ItWorks%2001b.gif)

# metashape
geometry clustering of shapes based on trained features

The goal is to get a set of geometries and cluster them to see patterns in geometric shapes.

## Initial Primitives
As a prototype, we developed a sample set of 16 elements that were categorized into cones, cylinders, spheres, and boxes.


## Initial Clustering
This set was trained in scikit-learn and Accord.NET through dodo, lunchbox, owl. Owl fit our needs in predictive modeling most effectively.

## Shape Analysis
Shape grammar has been notoriously difficult to quantify over the years manually, so machine learning is a great application of this

### Consistent Geometry Analysis
First, we take a dodecahedron to reduce polar biases and perform raycasting to determine vertex distances.

We also create a bounding box and then slice the building into upper, middle, and low slices as well as into levels describing terraces.

Additionally, we develop a contour and create a mesh to consistently calculate volume and area of the geometry.

### Geometric Properties
The general properties we have focused on:
- volume
- surface area
- centroids
- orientation
- ratios of properties

## Machine Learning
To categorize the building shapes, we used a clustering algorithm that would automatically group buildings based on their geometric properties.

For clustering algorithms, we initially tried a regression classification to test plugins, but decided that [Owl](http://www.food4rhino.com/app/owl) was the best solution for our use case. We used the following features:

- Area
- Aspect Ratios
- Centroid
- Eccentricity
- Orientation
- Slice Area
- Surface to Volume Ratio
- Terraces
- Vertex Mean Distance
- Vertex Farthest Distance
- Raycasting
- Volume to Bounding Box Ratio
- Volume

These provided us with enough features to distinguish differences between surrounding buildings.

## Future Work
We hope to include further feature analysis for our machine learning algorithms.
