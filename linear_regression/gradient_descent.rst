
Gradient Descent
----------------

It starts with a **random guess** and performs minimization steps
until it reaches optimal values for the coefficients.

The Gradient Descent algorithm works like this:

::
   
   1. set all model coefficients to random values
   2. calculate the partial derivative of the loss function (the MSE) by each coefficient (the Jacobian). This is also called the **gradient** :math:`\triangledown loss(\omega)`
   3. multiply the derivatives with a **learning rate** :math:`\eta`
   4. modify the coefficients by the modified derivatives
   5. repeat steps 2-4 until the algorithm converges

   The key equation for calculting the weight modification :math:`\triangle \omega` is:

   .. math::

      \triangle \omega = -\eta \triangledown loss(\omega)
