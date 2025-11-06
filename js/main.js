// Mobile Menu Toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    hamburger.classList.toggle('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-menu a').forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        hamburger.classList.remove('active');
    });
});

// Navbar scroll effect
let lastScroll = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 100) {
        navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    }

    lastScroll = currentScroll;
});

// ROI Calculator
const proceduresInput = document.getElementById('procedures');
const rsiRateInput = document.getElementById('rsi-rate');

function calculateROI() {
    const procedures = parseFloat(proceduresInput.value) || 0;
    const rsiRate = parseFloat(rsiRateInput.value) || 0;

    // Calculate expected RSI cases based on rate per 5,500 procedures
    const expectedCases = (procedures / 5500) * rsiRate;

    // Average cost per RSI incident
    const costPerIncident = 200000;

    // Calculate potential annual cost from RSI incidents
    const annualRsiCost = expectedCases * costPerIncident;

    // SurgiGuard AI system cost (example pricing)
    const systemCost = 50000;

    // Calculate net savings
    const netSavings = annualRsiCost - systemCost;

    // Calculate ROI percentage
    const roiPercentage = systemCost > 0 ? ((netSavings / systemCost) * 100) : 0;

    // Update display
    document.getElementById('expected-cases').textContent = expectedCases.toFixed(2);
    document.getElementById('annual-cost').textContent = `$${annualRsiCost.toLocaleString('en-US', {maximumFractionDigits: 0})}`;
    document.getElementById('system-cost').textContent = `$${systemCost.toLocaleString('en-US')}`;
    document.getElementById('net-savings').textContent = `$${netSavings.toLocaleString('en-US', {maximumFractionDigits: 0})}`;
    document.getElementById('roi-percentage').textContent = `${roiPercentage.toFixed(0)}%`;
}

// Add event listeners to calculator inputs
if (proceduresInput && rsiRateInput) {
    proceduresInput.addEventListener('input', calculateROI);
    rsiRateInput.addEventListener('input', calculateROI);

    // Calculate on page load
    calculateROI();
}

// Contact Form Handling
const contactForm = document.getElementById('contact-form');
const formMessage = document.getElementById('form-message');

if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Get form data
        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            phone: document.getElementById('phone').value,
            hospital: document.getElementById('hospital').value,
            title: document.getElementById('title').value,
            procedures: document.getElementById('procedures').value,
            message: document.getElementById('message').value
        };

        // Show loading state
        const submitButton = contactForm.querySelector('button[type="submit"]');
        const originalButtonText = submitButton.textContent;
        submitButton.textContent = 'Sending...';
        submitButton.disabled = true;

        // Simulate form submission (replace with actual API call)
        setTimeout(() => {
            // Show success message
            formMessage.className = 'form-message success';
            formMessage.textContent = 'Thank you! We\'ll contact you within 24 hours to schedule your demo.';

            // Reset form
            contactForm.reset();

            // Reset button
            submitButton.textContent = originalButtonText;
            submitButton.disabled = false;

            // Hide message after 5 seconds
            setTimeout(() => {
                formMessage.style.display = 'none';
            }, 5000);
        }, 1500);

        // In production, replace the above with actual API call:
        /*
        try {
            const response = await fetch('/api/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            if (response.ok) {
                formMessage.className = 'form-message success';
                formMessage.textContent = 'Thank you! We\'ll contact you within 24 hours to schedule your demo.';
                contactForm.reset();
            } else {
                throw new Error('Form submission failed');
            }
        } catch (error) {
            formMessage.className = 'form-message error';
            formMessage.textContent = 'Sorry, there was an error. Please try again or email us directly at support@deanware.com';
        } finally {
            submitButton.textContent = originalButtonText;
            submitButton.disabled = false;
        }
        */
    });
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));

        if (target) {
            const offsetTop = target.offsetTop - 80; // Account for fixed navbar
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in-up');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe all cards and sections for animation
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll(
        '.problem-card, .feature-card, .testimonial-card, .tech-item, .solution-text, .solution-visual'
    );

    animatedElements.forEach(el => observer.observe(el));
});

// Tracking demo animation
function animateTrackingDemo() {
    const instrumentItems = document.querySelectorAll('.instrument-item');

    instrumentItems.forEach((item, index) => {
        setTimeout(() => {
            item.style.opacity = '0';
            item.style.transform = 'translateX(-20px)';

            setTimeout(() => {
                item.style.transition = 'all 0.5s ease';
                item.style.opacity = '1';
                item.style.transform = 'translateX(0)';
            }, 100);
        }, index * 200);
    });
}

// Run tracking animation when section is visible
const trackingDemo = document.querySelector('.tracking-demo');
if (trackingDemo) {
    const trackingObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateTrackingDemo();
                trackingObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    trackingObserver.observe(trackingDemo);
}

// Stats counter animation
function animateCounter(element, target, duration = 2000) {
    const start = 0;
    const increment = target / (duration / 16);
    let current = start;

    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            element.textContent = target;
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(current);
        }
    }, 16);
}

// Animate stats when hero section is visible
const heroStats = document.querySelectorAll('.stat-number');
if (heroStats.length > 0) {
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const statsData = [
                    { element: heroStats[0], value: '5,500+' },
                    { element: heroStats[1], value: '$200K' },
                    { element: heroStats[2], value: '99.9%' }
                ];

                // Simple fade in effect
                heroStats.forEach((stat, index) => {
                    setTimeout(() => {
                        stat.style.opacity = '0';
                        stat.style.transform = 'translateY(20px)';

                        setTimeout(() => {
                            stat.style.transition = 'all 0.6s ease';
                            stat.style.opacity = '1';
                            stat.style.transform = 'translateY(0)';
                        }, 100);
                    }, index * 200);
                });

                statsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    const heroSection = document.querySelector('.hero');
    if (heroSection) {
        statsObserver.observe(heroSection);
    }
}

// Add active state to nav links based on scroll position
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-menu a[href^="#"]');

window.addEventListener('scroll', () => {
    let current = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;

        if (window.pageYOffset >= sectionTop - 100) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// Console greeting
console.log('%cSurgiGuard AI', 'color: #0066cc; font-size: 24px; font-weight: bold;');
console.log('%cAdvancing surgical safety through AI', 'color: #00cc88; font-size: 14px;');
console.log('%cInterested in joining our team? Email support@deanware.com', 'color: #666; font-size: 12px;');
