# users/throttles.py

from rest_framework.throttling import ScopedRateThrottle


class OTPRateThrottle(ScopedRateThrottle):
    """
    Tight throttle for OTP-generating endpoints (register/verify/resend).

    Uses the 'otp' scope configured in REST_FRAMEWORK['DEFAULT_THROTTLE_RATES']
    (5/hour by default) so a single client can't spam OTP emails.
    """

    scope = "otp"


class AuthRateThrottle(ScopedRateThrottle):
    """
    Throttle for login/token endpoints. Uses the 'auth' scope (20/min).
    """

    scope = "auth"
