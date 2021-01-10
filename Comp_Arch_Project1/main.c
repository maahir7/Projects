 #include <stdio.h>
 #include "dot_product.h"
 #include <stdlib.h>

float dot_product(float *v1, float *v2, int length){
    float result;
    int i;
    __m128 xmm1, xmm2, xmm3 ,xmm4;
   // xmm3= _mm_setzero_ps();
    xmm4= _mm_setzero_ps();  //sets sum to zero
    for(i=0; i<VSIZE; i+=4)

  {

  xmm1 = _mm_load_ps(v1 +i); //loads aligned array a into  xmm1   xmm1 = v1[0]  v1[1]  v1[2]  v1[3]

  xmm2 = _mm_load_ps(v2 +i); //loads aligned array a into  xmm1   xmm1 = v2[0]  v2[1]  v2[2]  v2[3]


  xmm3 = _mm_mul_ps(xmm1, xmm2); //performs multiplication  xmm3 = v1[0]*v2[0]  v1[1]*v2[1]   v1[2]*v2[2]   v1[3]*v2[3]

  xmm3 =_mm_hadd_ps(xmm3, xmm3); //performs horizontal addition
                                 //num3=  v1[3]*v2[3]+ v1[2]*v2[2]  v1[1]*v2[1]+v1[0]*v2[0]  v1[3]*v2[3]+ v1[2]*v2[2]  v1[1]*v2[1]+v1[0]*v2[0]

  xmm4 = _mm_add_ps(xmm4, xmm3); //performs vertical addition
  }

   xmm4 = _mm_hadd_ps(xmm4, xmm4);

  _mm_store_ss(&result,xmm4);

  return result;
}
