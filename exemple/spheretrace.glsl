#define MAX_DISTANCE 512.0
#define MAX_STEPS 256
#define EPSILON 0.001

vec4 spheretrace(in vec3 ro, in vec3 rd, out bool hit)
{
    vec3 p = ro;
    float d = SDF(p);
    float dAcc = d;
    hit = false;
    for(int i = 0; i < MAX_STEPS; ++i)
    {
        if(d <= EPSILON || d >= MAX_DISTANCE)
        {
            hit = d <= EPSILON;
            break;
        }

        p += d * rd;
        d = SDF(p);
        dAcc += d;
    }
    return vec4(p, dAcc);
}